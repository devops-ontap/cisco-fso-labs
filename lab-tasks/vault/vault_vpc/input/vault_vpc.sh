#!/bin/sh
export AWS_PAGER=""
#This is required for vault
python3 -m pip install hvac
python3 -m pip install async-hvac
setcap cap_ipc_lock= /usr/bin/vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
python3 vault_vpc.py





