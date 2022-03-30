#!/bin/sh
export AWS_PAGER=""
pip3 install paramiko
#apt -y install ncurses-term
#Call the vault and set the SSH key to env var
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
export TE_GROUP=$TE_GROUP
vault login --no-print $SSH_TOKEN
vault kv get --field=ssh-key concourse/cisco-fso-labs/$NAME >> sshkey.pem
SSHKEY='sshkey.pem'
#TRY THIS AND SEE IF PYTHON AN INGEST IT
#PRIVATE_KEY=$(vault kv get --field=ssh-key concourse/cisco-fso-labs/$NAME)
#Add the IPs in the hostfile to the known_hosts
chmod 400 sshkey.pem
mkdir ~/.ssh
touch ~/.ssh/known_hosts
echo "${SSHKEY}" | ssh-add -
for server in $(cat hostfile)
do
  ssh-keyscan -H "$server" >> ~/.ssh/known_hosts
  ssh -i sshkey.pem ubuntu@"$server" env TE_GROUP=$TE_GROUP
done
#Need to figure out what is required for the Instance to be able to set the env var or call vault to pass in the token
#remotely set the VAR for now
#ssh username@hostname env VAR1=VALUE1

python3 configure_te_agents.py



