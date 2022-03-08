#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
pip3 install paramiko
apt -y install ncurses-term
/usr/local/bin/python -m pip install --upgrade pip
curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
ssh-keyscan -H 3.145.46.2 >> ~/.ssh/known_hosts
scp -i us-east-2a.pem -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null install_thousandeyes.sh ubuntu@3.145.46.2:/tmp
python3 configure_te.py

