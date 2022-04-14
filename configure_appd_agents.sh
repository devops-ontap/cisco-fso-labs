#!/bin/sh
export AWS_PAGER=""
#!/bin/sh
pip3 install paramiko
#Call the vault and set the SSH key to env var
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
export APPD_ACCESS=$APPD_ACCESS
export APPD_OATH=$APPD_OATH
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
  scp -i sshkey.pem controller-info.xml ubuntu@"$server":~/
done
python3 configure_appd_agents.py


