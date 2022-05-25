#!/bin/sh
cd input
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
keyid=$(vault kv get --field=key concourse/cisco-fso-labs/intersight/keyid)
export keyid=$keyid
rsa=$(vault kv get --field=key concourse/cisco-fso-labs/intersight/rsa)
export rsa=$rsa
pip3 install cryptography
pip3 install git+https://github.com/CiscoDevNet/intersight-python
python3 contractstatus.py
python3 new.py