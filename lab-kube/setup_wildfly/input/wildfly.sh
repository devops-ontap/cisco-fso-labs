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
kubectl create ns wildfly
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update
helm -n wildfly upgrade wildfly bitnami/wildfly -f values.yaml --set wildflyUser=manager,wildflyPassword=wildfly
kubectl -n wildfly get svc wildfly -w











