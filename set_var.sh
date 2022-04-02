#!/bin/sh
touch .bash_profile
export VAULT_ADDR=http://vault.devops-ontap.com:8200
echo $VAULT_ADDR
env VAULT_ADDR=http://vault.devops-ontap.com:8200