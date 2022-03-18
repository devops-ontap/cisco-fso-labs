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
#must to a for each here to copy the install file to each instance...

#ssh-keyscan -H localhost >> ~/.ssh/known_hosts
#scp -i sshkey.pem -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null install_thousandeyes.sh ubuntu@IP:/tmp
python3 configure_te_agents.py


