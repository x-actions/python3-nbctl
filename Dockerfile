FROM ubuntu:22.04

# Dockerfile build cache 
ENV REFRESHED_AT 2023-05-07

LABEL "com.github.actions.name"="nbctl"
LABEL "com.github.actions.description"="nbctl"
LABEL "com.github.actions.icon"="chevrons-right"
LABEL "com.github.actions.color"="blue"
LABEL "repository"="http://github.com/x-actions/python3-nbctl"
LABEL "homepage"="http://github.com/x-actions/python3-nbctl"
LABEL "maintainer"="xiexianbin<me@xiexianbin.cn>"

LABEL "Name"="nbctl"
LABEL "Version"="1.0.0"

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

# apt install -y docker-ce docker-ce-cli containerd.io; systemctl start docker
RUN apt update && \
    apt install -y git python3 python3-pip skopeo jq && \
    cd ~ && \
    git clone https://github.com/x-actions/python3-nbctl.git && \
    cd python3-nbctl && \
    git checkout v1 && \
    pip3 install -r requirements.txt && \
    python3 setup.py --version && \
    python3 setup.py install

ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh

WORKDIR /github/workspace
ENTRYPOINT ["/entrypoint.sh"]
