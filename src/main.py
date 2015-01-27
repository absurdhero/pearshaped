#!/usr/bin/python3

# Checks out a git repo to a local directory if it doesn't exist.
# If it does exist, it pulls it.
# Builds a docker image based on the chose toolchain in the project's config.
# Mounts the repo in the container and invokes the builder.
# The builder executes the scripts in .pearshaped.yml or .travis.yml (in that order).
# Reports build results on stdout.

import os

from lib import configure, executor, repo

repo_dir = repo.sync('/build/projects', os.getenv("REPO_URL"))

config = configure.parse(configure.find(repo_dir))

home_path = os.getenv('PEARSHAPED_HOME')
exec = executor.Executor(home_path, repo_dir, config)
success = exec.run()

if not success:
    exit(1)
