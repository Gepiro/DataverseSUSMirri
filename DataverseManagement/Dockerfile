FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y gcc make libbz2-dev libncursesw5-dev liblzma-dev bzip2 curl

# python3 installation
RUN apt-get install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev -y
COPY ./Python-3.11.2.tar.xz /tmp/Python-3.11.2.tar.xz
RUN tar -xf /tmp/Python-3.11.2.tar.xz

WORKDIR /Python-3.11.2
RUN ./configure --enable-optimizations
RUN make install

RUN pip3 install pyDataverse
WORKDIR /

# copy data
COPY script /script
# COPY results /results 
# COPY metadata.json / 
# COPY dataverse.json /

ENTRYPOINT ["python3", "/script/main.py"]