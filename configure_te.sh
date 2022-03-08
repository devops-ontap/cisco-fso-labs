#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
pip3 install paramiko
apt -y install ncurses-term
apt -y install -y openssh-clients
ssh-keyscan -H 3.145.46.2 >> ~/.ssh/known_hosts
python3 configure_te.py

