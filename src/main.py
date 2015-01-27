#!/usr/bin/python3

# Checks out a git repo to a local directory if it doesn't exist.
# If it does exist, it pulls it.
# Builds a docker image based on the chose toolchain in the project's config.
# Mounts the repo in the container and invokes the builder.
# The builder executes the scripts in .pearshaped.yml or .travis.yml (in that order).
# Reports build results on stdout.

import os
import sys

from lib import configure, executor, repo, projects


home_path = os.getenv('PEARSHAPED_HOME')

if not os.path.exists('/build/config.yml'):
    print("config.yml missing in PEARSHAPED_HOME [%s]" % home_path, file=sys.stderr)
    exit(127)

for project in projects.each('/build'):
    print("executing " + project.name)


    repo_dir = repo.sync('/build/projects', project.repo_url)

    config = configure.parse(configure.find(repo_dir))

    exec = executor.Executor(home_path, repo_dir, config)
    success = exec.run()

    if not success:
        exit(1)
