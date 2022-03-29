#!/bin/sh
echo "echo-ing out the $NAME as set in pipeline set step with var"
echo $NAME
export AWS_PAGER=""
rm -rf __pycache__
apt -y update
#apt -y install jq
#curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add -
#apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
#apt-get update && apt-get install vault
setcap cap_ipc_lock= /usr/bin/vault
#apt -y install jq
python3 aws_key.py
PRIVATE_KEY=$(ls *.pem)
touch touch $PRIVATE_KEY.json
awk 'NF {sub(/\r/, ""); printf "%s\\n",$0;}' $PRIVATE_KEY >  $PRIVATE_KEY.json


#Later iteration, set up access so that the key can be written to vault for the team, for now manually add it.
#This is where send the key to the vault under the team name
export VAULT_ADDR=http://vault.devops-ontap.com:8200
#get the vault address from the vault via var
#How to logon to vault with the cli to do this....
#vault kv put kv-v1/prod/cert/mysql cert=@cert.pem
vault login $SSH_TOKEN
vault kv put concourse/cisco-fso-labs/$NAME ssh-key=@$PRIVATE_KEY









