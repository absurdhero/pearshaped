#!/usr/bin/python3

# Checks out a git repo to a local directory if it doesn't exist.
# If it does exist, it pulls it.
# Builds a docker image based on the chose toolchain in the project's config.
# Mounts the repo in the container and invokes the builder.
# The builder executes the scripts in .pearshaped.yml or .travis.yml (in that order).
# Reports build results on stdout.

import os
import sys

from lib import configure, executor, repo, projects, build_info

home_path = os.getenv('PEARSHAPED_HOME')


def build_all():
    if not os.path.exists('/build/config.yml'):
        print("config.yml missing in PEARSHAPED_HOME [%s]" % home_path, file=sys.stderr)
        exit(127)

    for project in projects.each('/build'):
        print("executing " + project.name)

        project_dir = os.path.join('/build/projects', project.name)

        try:
            os.makedirs(os.path.join(project_dir, 'builds'))
        except FileExistsError:
            pass

        build_id = "1"
        with open(os.path.join(project_dir, 'build_id'), 'a+') as id_file:
            id_file.seek(0)
            line = id_file.readline()

            if len(line) != 0:
                build_id = line.strip()
                id_file.seek(0)
                id_file.truncate(0)

            id_file.write(str(int(build_id) + 1))

        repo_dir = repo.sync(project_dir, project.repo_url)
        config = configure.parse(configure.find(repo_dir))

        info = build_info.BuildInfo(home_path, project_dir, build_id, config)

        try:
            os.mkdir(info.build_dir)
        except FileExistsError:
            pass


        exec = executor.Executor(info)
        status = exec.run()

        if not status.success:
            exit(1)

if __name__ == "__main__":
    build_all()