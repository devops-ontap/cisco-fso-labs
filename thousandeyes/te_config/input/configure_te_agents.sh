#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
apt -y install ncurses-term
python3 configure_te_agents.py


