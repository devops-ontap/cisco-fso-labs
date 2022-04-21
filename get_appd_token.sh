#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__
export SSH_TOKEN=$SSH_TOKEN
export APPD_SECRET=$APPD_SECRET
vault login --no-print $SSH_TOKEN
python3 get_token.py
echo $TOKEN
vault kv put concourse/cisco-fso-labs/appd-oath key=token