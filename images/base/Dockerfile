FROM ubuntu:14.04.1
MAINTAINER absurdhero
RUN apt-get update
RUN apt-get upgrade -y

# required to run the builder
RUN apt-get install -qy python3 python3-pip git
RUN pip3 install pyYAML

# common expected packages for a build environment
RUN apt-get install -qy scons cmake curl wget rsync openssl xvfb

RUN apt-get clean

ADD travis_retry /bin/
