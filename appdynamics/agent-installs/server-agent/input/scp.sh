#!/bin/sh
printenv
echo "${SSHKEY}" | ssh-add -
user='ubuntu'
hostfile='hostfile'
apt-get -yqq install ssh
for server in $(cat hostfile)
do
  ssh-keyscan -H "$server" >> ~/.ssh/known_hosts
done
wait