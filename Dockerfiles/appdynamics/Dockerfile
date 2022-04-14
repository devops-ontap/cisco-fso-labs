FROM ubuntu:20.04
MAINTAINER Sherri Conrod <devopsontap@yahoo.com>
#appdynamics build oci
#update your docker image with your required python modules and other libraries - remember to manuall increment the tag version until symantec verioning is applied
#Required to use your params file for your docker repo with creds - enter into vault too.

ENV DEBIAN_FRONTEND noninteractive

RUN apt  update && \
  apt -y install software-properties-common build-essential vim unzip curl python3 python3-pip glibc-source groff less git-core jq openssh-client openssl make telnet ncurses-term git rpm default-jre procps && \
  apt clean && \
  rm -rf /var/lib/apt/lists/* \

RUN pip3 install urllib3 paramiko ncurses-term subprocess

RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
  apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
  apt update && apt -y install vault \






