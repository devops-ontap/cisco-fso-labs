#!/bin/sh
cd input
export AWS_PAGER=""
#!/bin/sh
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
touch var
echo $APPD_ACCESS > var
echo $APPD_OATH > var
for server in $(cat hostfile)
do
  ssh-keyscan -H "$server" >> ~/.ssh/known_hosts
# ssh -i sshkey.pem ubuntu@"$server" env TE_GROUP=$TE_GROUP
  scp -i sshkey.pem var ubuntu@"$server":~/
  scp -i sshkey.pem controller-info.xml ubuntu@"$server":~/
done
#python3 configure_appd_agents.py


