#!/bin/sh
pwd
ls -la
chmod 400 *.pem
export AWS_PAGER=""
#apt -y install ncurses-term
#Call the vault and set the SSH key to env var

#See if it can read in the key value
echo $PRIVATE_KEY

#export VAULT_ADDR=$VAULT_ADDR
#vault login --no-print $SSH_TOKEN
#vault kv get concourse/cisco-fso-labs/$NAME ssh-key=@$PRIVATE_KEY
python3 configure_te_agents.py


