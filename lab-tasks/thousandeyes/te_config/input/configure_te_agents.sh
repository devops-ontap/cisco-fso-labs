#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
apt -y install ncurses-term
#Call the vault and set the SSH key to env var
python3 configure_te_agents.py


