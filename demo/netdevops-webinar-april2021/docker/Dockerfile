FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=America/Detriot
ENV ANSIBLE_CONFIG=/workspace/ansible.cfg
RUN apt-get update && apt-get install -y \
    tzdata \
    python3 \
    python3-pip \
    net-tools \
    iputils-* \
    git-all
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN ansible-galaxy collection install netbox.netbox
RUN ansible-galaxy collection install arista.eos
RUN echo 'alias python="python3"' >> ~/.bashrc
RUN echo 'alias pip="pip3"' >> ~/.bashrc