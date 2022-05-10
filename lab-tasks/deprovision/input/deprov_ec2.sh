#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
python3 deprov_ec2.py
