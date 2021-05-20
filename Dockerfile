FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libcurl4
RUN apt-get install -y curl
RUN apt-get install -y software-properties-common vim python3-pip
RUN apt-get install -y python3

RUN curl -fsSL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

COPY backend/ /root/backend/
COPY frontend/ /root/frontend/
COPY main.c /root/main.c

RUN pip3 install -r /root/backend/requirements.txt

ENV UPLOAD_FOLDER=/root/backend/uploads
ENV npm_config_loglevel=silent

WORKDIR /root

RUN gcc main.c -o computer_vision_server
RUN rm main.c
