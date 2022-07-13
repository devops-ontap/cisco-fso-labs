#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x ./kops
mv ./kops /usr/local/bin/
vault login --no-print $SSH_TOKEN
mkdir ~/.kube
vault kv get -field kubeconfig concourse/cisco-fso-labs/lab-kube-config > ~/.kube/config
chmod 400 /root/.kube/config
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops export kubecfg --admin
helm repo add rocketchat https://rocketchat.github.io/helm-charts
helm repo update
kubectl create ns rocketchat
helm -n rocketchat delete rocketchat
kubectl -n rocketchat delete pvc --all
#helm -n rocketchat install rocketchat rocketchat/rocketchat --set mongodb.auth.password=$(echo -n $(openssl rand -base64 32)),mongodb.auth.rootPassword=$(echo -n $(openssl rand -base64 32))
#helm -n rocketchat upgrade rocketchat rocketchat/rocketchat --set mongodb.auth.password=$(echo -n $(openssl rand -base64 32)),mongodb.auth.rootPassword=$(echo -n $(openssl rand -base64 32)) -f values.yaml
#helm -n rocketchat upgrade rocketchat rocketchat/rocketchat --set host=a0027ea6f790b4222a90f03dc88b707e-1027696678.us-east-2.elb.amazonaws.com --set ingress.enabled=true stable/rocketchat -f values.yaml
helm -n rocketchat upgrade rocketchat rocketchat/rocketchat --set mongodb.auth.password=$(echo -n $(openssl rand -base64 32)),mongodb.auth.rootPassword=$(echo -n $(openssl rand -base64 32)) --set host=chat.devops-ontap.com --set ingress.enabled=true rocketchat/rocketchat










