#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
pip3 install paramiko
python3 get_token.py
export SSH_TOKEN=$SSH_TOKEN
