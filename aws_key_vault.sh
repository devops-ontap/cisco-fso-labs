#!/bin/sh
export AWS_PAGER=""
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
cd git-resource
python3 aws_key.py
cat *.pem
PRIVATE_KEY=$(ls *.pem)
echo $PRIVATE_KEY
#touch touch $PRIVATE_KEY.json
#awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' $PRIVATE_KEY >  $PRIVATE_KEY.json
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
vault kv put concourse/cisco-fso-labs/$NAME ssh-key=@$PRIVATE_KEY









