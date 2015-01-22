FROM ubuntu:14.04.1
MAINTAINER absurdhero
RUN apt-get update
RUN apt-get upgrade -y

# common expected packages for a build environment
RUN apt-get install -qy build-essential make scons cmake curl wget rsync openssl xvfb git golang python nodejs npm sqlite

RUN apt-get clean

RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby

ADD travis_retry /bin/

RUN ln -s /usr/bin/nodejs /usr/bin/node
