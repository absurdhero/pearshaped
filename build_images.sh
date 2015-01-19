#!/bin/bash

# build the base image and all language-specific images

cd images

search=*

if [ $1 ]; then
    search=$1;
fi

for d in `find $search -type d`; do
    if [[ -e ./$d/Dockerfile ]] ; then
        tag=`echo $d | tr / -`
        echo "building $tag"
        (cd $d; docker build -t "shipbuilder_$tag" --force-rm=true .)
    fi
done

