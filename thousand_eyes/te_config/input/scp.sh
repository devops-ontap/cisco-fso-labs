#!/bin/sh
#ssh-keyscan -H 3.21.246.206 >> ~/.ssh/known_hosts
#scp -i us-east-2a.pem -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null install_thousandeyes.sh ubuntu@3.21.246.206:/tmp
for server in $(cat hostfile)
do
  ssh-keyscan -H "$servr" >> ~/.ssh/known_hosts
done
wait

for server in $(cat hostfile)
do
  scp -i us-east-2a.pem -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null install_thousandeyes.sh "$server":/tmp/ &
done
wait