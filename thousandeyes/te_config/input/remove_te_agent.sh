#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
/usr/local/bin/python -m pip install --upgrade pip
pip3 install paramiko
pip3 install requests
apt -y install ncurses-term
curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
ssh-keyscan -H 3.21.246.206 >> ~/.ssh/known_hosts
scp -i us-east-2a.pem -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null install_thousandeyes.sh ubuntu@3.21.246.206:/tmp
python3 remove_te_agent.py
