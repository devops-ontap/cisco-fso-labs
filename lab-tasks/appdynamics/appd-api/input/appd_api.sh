#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
pip3 install paramiko
python3 get_token.py
export SSH_TOKEN=$SSH_TOKEN
#vault login --no-print $SSH_TOKEN
vault login $SSH_TOKEN
vault kv put concourse/cisco-fso-labs/appd-oath key=token