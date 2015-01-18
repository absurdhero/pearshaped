#!/bin/sh

docker build -q -t shipbuilder --force-rm=true .

#docker run -it shipbuilder /bin/sh
docker run -i shipbuilder
