#!/bin/sh
export AWS_PAGER=""
rm -rf __pycache__
apt -y update
apt -y install jq
apt -y install vault
apt -y install jq
python3 aws_key.py
#name the pem key with the name var
#See how the pem key is named
echo $name
ls -la *.pem
cat *.pem
PRIVATE_KEY='ssh-key.pem'
#echo "echo-ing out the var $PRIVATE_KEY
echo $PRIVATE_KEY
touch ssh-key.json
awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' $PRIVATE_KEY > ssh-key.json
#Later iteration, set up access so that the key can be written to vault for the team, for now manually add it.
#This is where send the key to the vault under the team name
export VAULT_API_ADDR=http://vault.devops-ontap.com:8200
#get the vault address from the vault via var
#How to logon to vault with the cli to do this....
export VAULT_TOKEN=$VAULT_TOKEN
#vault kv put kv-v1/prod/cert/mysql cert=@cert.pem
vault kv put concourse/cisco-fso-labs/ssh-cert cert=@ssh-key.pem









