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
chmod 400 sshkey.pem
mkdir ~/.ssh
touch ~/.ssh/known_hosts
echo "${SSHKEY}" | ssh-add -
for server in $(cat hostfile)
do
  ssh-keyscan -H "$server" >> ~/.ssh/known_hosts
done
python3 delete_te_agents.py



