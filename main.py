#!/usr/bin/python3

# checks out a git repo to a local directory if it doesn't exist
# if it does exist, it pulls it.

# executes .ship.yml or .travis.yml (in that order)

# reports build results on stdout

import os

from lib import repo, executor

repo_dir = repo.sync()

config = executor.parse_shipconfig(executor.find_config(repo_dir))

os.chdir(repo_dir)

success = executor.run(config)

if not success:
    exit(1)
