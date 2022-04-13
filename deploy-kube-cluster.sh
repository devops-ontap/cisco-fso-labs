#Install kubectl
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apk-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apk update && sudo apt-get install vault
aws configure
kubectl --version
kops --version

#in aws deploy its an ec2 key here its an iam key
#try rotate key or something...
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
vault kv put concourse/cisco-fso-labs/lab-cops-iam ssh-key=@$PRIVATE_KEY