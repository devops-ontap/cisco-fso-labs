#!/bin/sh
#printenv
export AWS_PAGER=""
rm -rf __pycache__
apt -y update
#This is required for vault
setcap cap_ipc_lock= /usr/bin/vault
python3 aws_key.py
PRIVATE_KEY=$(ls *.pem)
cat $PRIVATE_KEY
#This may be deprecated in the future
touch touch $PRIVATE_KEY.json
awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' $PRIVATE_KEY >  $PRIVATE_KEY.json
#Consider having each Lab User Setup with their own Team in CI and Vault
export VAULT_ADDR=$VAULT_ADDR
#Sample Command to logon to vault with the cli to do this....
#vault kv put kv-v1/prod/cert/mysql cert=@cert.pem
vault login $SSH_TOKEN --no-print
vault kv put concourse/cisco-fso-labs/$NAME ssh-key=@$PRIVATE_KEY









