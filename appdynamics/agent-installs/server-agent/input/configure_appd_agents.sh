#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
/usr/local/bin/python -m pip install --upgrade pip
pip3 install paramiko
pip3 install requests
pip3 install urllib3
apt -y install unzip
apt -y install ncurses-term
apt -y install rpm
python3 configure_appd_agents.py


