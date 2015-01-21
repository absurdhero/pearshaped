#!/bin/sh

set -e -x

if [ ! $REPO_DIR ]; then
    REPO_DIR=$HOME/.shipbuilder/repos
fi
docker build -q -t shipbuilder --force-rm=true .
docker run --name shipbuilder-controller -v $REPO_DIR:/repos -v /var/run/docker.sock:/var/run/docker.sock -e "REPO_URL=${REPO_URL}" shipbuilder
