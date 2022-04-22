#!/bin/sh
cd input
apt -y update && apt -y upgrade
pip3 install paramiko
#apt -y install ncurses-term
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
vault kv get --field=ssh-key concourse/cisco-fso-labs/$NAME >> sshkey.pem
APPD_OATH_TOKEN=$(vault kv get --field=token concourse/cisco-fso-labs/appd-oath)
export APPD_OATH_TOKEN=$APPD_OATH_TOKEN
curl -L -O -H "Authorization: Bearer $APPD_OATH_TOKEN;" "https://download.appdynamics.com/download/prox/download-file/machine/22.2.0.3282/appdynamics-machine-agent-22.2.0.3282.x86_64.rpm"
SSHKEY='sshkey.pem'
chmod 400 sshkey.pem
mkdir ~/.ssh
touch ~/.ssh/known_hosts
echo "${SSHKEY}" | ssh-add -
for server in $(cat hostfile)
do
  ssh-keyscan -H "$server" >> ~/.ssh/known_hosts
  scp -i sshkey.pem controller-info.xml ubuntu@"$server":~/
  scp -i sshkey.pem appdynamics-machine-agent-22.2.0.3282.x86_64.rpm ubuntu@"$server":~/
done
python3 appd_install_agents.py