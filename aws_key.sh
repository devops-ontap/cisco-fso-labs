#!/bin/sh
export AWS_PAGER=""
rm -rf __pycache__
pip3 install vault-cli
python3 aws_key.py
#name the pem key with the name var
#See how the pem key is named
echo $name
ls -la *.pem
cat *.pem
mov *.pem $name.pem
#This is where send the key to the vault under the team name
export VAULT_API_ADDR=http://vault.devops-ontap.com:8200
vault kv put concourse/main/ssh-cert cert=@us-east-2a.pem








