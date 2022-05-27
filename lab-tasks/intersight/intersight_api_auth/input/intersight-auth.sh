#!/bin/sh
cd input
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
pip3 install cryptography
pip3 install git+https://github.com/CiscoDevNet/intersight-python
keyid=$(vault kv get --field=keyid concourse/cisco-fso-labs/intersight/keyid_v2)
export keyid=$keyid
vault kv get --field=secret concourse/cisco-fso-labs/intersight/secret_v2 > SecretKey.txt
export secret=$secret
python3 PhysicalSummaries_v2.py
