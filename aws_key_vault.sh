#!/bin/sh
#printenv
export AWS_PAGER=""
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
python3 aws_key.py
cp *.pem ssh-key.pem
#This may be deprecated in the future
touch touch $PRIVATE_KEY.json
awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' $PRIVATE_KEY >  $PRIVATE_KEY.json
#Consider having each Lab User Setup with their own Team in CI and Vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
vault kv put concourse/cisco-fso-labs/$NAME ssh-key=@ssh-key.pem









