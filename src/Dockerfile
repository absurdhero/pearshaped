FROM orchard-language-python3
MAINTAINER absurdhero

RUN apt-get install -qy docker.io git

RUN pip3 install pyYAML
ADD main.py /root/
ADD lib /root/lib

CMD /root/main.py
