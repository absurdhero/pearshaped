shipdock
========

A docker-based build framework and continuous-integration system which runs
builds in isolated containers. shipdock itself also runs inside a container.

In simple cases, shipbuilder acts as a drop-in replacement for Travis CI.
It will read either its own `.ship.yml` config file or `.travis.yml`.
Ease of migration from Travis is a goal but 100% compatibility is currently
not.

Running inside docker:

    REPO_URL=https://github.com/my/repo" ./run.sh

Running outside of docker:

    REPO_URL="https://github.com/my/repo" python3 ./main.py

Building the base docker image and each language image:

    ./build_images.sh

Build a single language image:

    ./build_images.sh language/python

Build the base image:

    ./build_images.sh base

