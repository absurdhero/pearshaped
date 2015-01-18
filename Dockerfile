FROM shipbuilder-base
MAINTAINER absurdhero

RUN pip3 install pyYAML
ADD main.py /root/
ADD lib /root/lib

CMD /root/main.py
