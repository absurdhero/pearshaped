#!/bin/sh

# run a local git daemon that exposes all repos under /opt/git

git daemon --export-all --reuseaddr --base-path=/opt/git

