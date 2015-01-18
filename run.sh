#!/bin/sh

docker build -q -t shipbuilder --force-rm=true .
docker run  shipbuilder
