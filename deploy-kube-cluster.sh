#Install kubectl
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
sudo apk-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
sudo apk update && sudo apt-get install vault
aws configure
kubectl --version
kops --version