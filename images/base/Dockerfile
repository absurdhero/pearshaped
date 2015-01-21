FROM ubuntu:14.04.1
MAINTAINER absurdhero
RUN apt-get update
RUN apt-get upgrade -y

# common expected packages for a build environment
RUN apt-get install -qy scons cmake curl wget rsync openssl xvfb

RUN apt-get clean

ADD travis_retry /bin/
