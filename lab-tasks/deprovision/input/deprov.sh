#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN

#Get all the vars from the vault
setcap cap_ipc_lock= /usr/bin/vault
vault login --no-print $SSH_TOKEN
vault kv get concourse/cisco-fso-labs/$NAME/ssh-key ssh-key=@$PRIVATE_KEY

#Will need at least one python script to poll for instance state change to terminated state before proceeding...
python3 deprov.py

#rest of shell commands make sure to update the aws region
