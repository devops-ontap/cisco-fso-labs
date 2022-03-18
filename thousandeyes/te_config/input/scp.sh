#!/bin/sh
printenv
echo "${SSHKEY}" | ssh-add -
echo -e "${SSHKEY//_/\\n}" > ~/.ssh/sshkey && chmod 400 ~/.ssh/sshkey
#key='key.pem'
user='ubuntu'
hostfile='hostfile'
apt-get -yqq install ssh
for server in $(cat hostfile)
do
  ssh-keyscan -H "$server" >> ~/.ssh/known_hosts
  scp -i $SSHKEY -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null install_thousandeyes.sh $user@$server:/tmp/ &
done
wait