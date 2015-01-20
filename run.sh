#!/bin/sh

docker build -q -t shipbuilder --force-rm=true .
docker run -v /var/run/docker.sock:/var/run/docker.sock -e "REPO_URL=${REPO_URL}" shipbuilder
