#!/bin/sh

docker build -q -t shipbuilder --force-rm=true .
docker run -e "REPO_URL=${REPO_URL}" shipbuilder
