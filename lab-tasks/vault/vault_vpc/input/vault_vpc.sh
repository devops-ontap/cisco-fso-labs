#!/bin/sh
export AWS_PAGER=""
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
VAULT_TOKEN=$(vault kv get --field=token concourse/cisco-fso-labs/ssh-token)
export VAULT_TOKEN=$VAULT_TOKEN
python3 vault_vpc.py





