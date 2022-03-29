#!/bin/sh
export AWS_PAGER=""
pip3 install paramiko
#apt -y install ncurses-term
#Call the vault and set the SSH key to env var
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
vault kv get concourse/cisco-fso-labs/$NAME ssh-key

#Get the Key from the Vault and Set it to an ENV VAR


#python3 configure_te_agents.py


