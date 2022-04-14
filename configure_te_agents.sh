#!/bin/sh
export AWS_PAGER=""
apt -y update && apt -y upgrade
pip3 install paramiko
#apt -y install ncurses-term
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
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
  scp -i sshkey.pem install_te.sh ubuntu@"$server":~/
done
python3 configure_te_agents.py



