#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
/usr/local/bin/python -m pip install --upgrade pip
pip3 install paramiko
pip3 install requests
pip3 install urllib3
apt -y install ncurses-term
chmod a+x scp.sh
./scp.sh
python3 configure_te_agents.py

