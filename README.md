pearshaped
==========

A docker-based build framework and continuous-integration system which runs
builds in isolated containers, saving the state after each step.
Pearshaped itself runs inside a container for easy deployment.

In simple cases, pearshaped acts as a drop-in replacement for Travis CI.
It will read either its own `.pearshaped.yml` config file or `.travis.yml`.
Ease of migration to/from Travis is a goal but 100% compatibility is not.

For Those Short on Time
-----------------------

After checking out this git repo here's how to build this project and
then run it on your repo that already has a pearshaped or travis config:

    mkdir ~/.pearshaped
    echo 'projects: {test: {repo: "https://github.com/my/repo"}}' > ~/.pearshaped/config.yml
    bin/build_images
    build=true bin/run


Commands
--------

Build docker image and run inside docker:

    build=true bin/run

Building the base docker image and all language images:

    bin/build_images

Build a single language image:

    bin/build_images language/python

Build the base image:

    bin/build_images base

Configuration
-------------

Add projects to pearshaped by editing `config.yml` under PEARSHAPED_HOME (`.pearshaped` by default)

`config.yml` are formatted like the following with one or more projects:

```yaml

projects:
    foo:
        repo: https://github.com/foo/foo

```

file layout:
```
$PEARSHAPED_HOME
├── projects
│   └── foo
└── config.yml
```

Toolchain Support
-----------------

pearshaped ships with support for several popular toolchains and versions.
Currently, the base VM is Ubuntu 14.04 with autotools, gcc, clang, go,
nodejs, and npm, and rvm installed for use by all configurations.

In addition, setting the 'language' property in the ship config to one
of the following performs additional actions:

golang:

    apt-get install -qy golang golang-go.tools

ruby (control the version with the 'rvm' property in your config):

    rvm install <version>
    gem install bundler rake

nodejs:

    apt-get install -qy nodejs npm

python:

    apt-get install -qy python python-dev
    pip install nose pytest mock wheel

python3:

    apt-get install -qy python3 python3-dev
    pip3 install nose pytest mock wheel
