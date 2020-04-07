FROM python:3-alpine3.6 

LABEL maintainer="Arista Ansible Team <ansible@arista.com>"
LABEL com.example.version="1.0.2"
LABEL vendor1="Arista"
LABEL com.example.release-date="2020-02-12"
LABEL com.example.version.is-production="False"

ENV PS1='\u@arista-avd-cvp-demo>'

WORKDIR /tmp

COPY requirements.txt .
RUN apk add --update --no-cache ca-certificates \
    openssh-client \
    build-base \
    gcc \
    g++ \
    make \
    python-dev \
    py-pip \
    libffi-dev \
    sshpass \
    libressl-dev
RUN pip install --upgrade pip && \
    pip install -r requirements.txt &&\
    apk del -r --purge gcc make g++ &&\
    rm -rf /source/* &&\
    rm -rf /var/cache/apk/* &&\
    rm -rf /tmp/*

WORKDIR /project
