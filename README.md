shipdock
========

A docker-based build framework and continuous-integration system which runs
builds in isolated containers, saving the state after each step.
shipdock also runs inside a container.

In simple cases, shipbuilder acts as a drop-in replacement for Travis CI.
It will read either its own `.ship.yml` config file or `.travis.yml`.
Ease of migration from Travis is a goal but 100% compatibility is currently
not.

Running inside docker:

    REPO_URL=https://github.com/my/repo" bin/run

Running outside of docker:

    REPO_URL="https://github.com/my/repo" REPO_DIR=~/.shipbuilder/repos python3 ./main.py

Building the base docker image and each language image:

    bin/build_images

Build a single language image:

    bin/build_images language/python

Build the base image:

    bin/build_images base

