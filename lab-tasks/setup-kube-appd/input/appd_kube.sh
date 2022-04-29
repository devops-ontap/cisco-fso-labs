#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x ./kops
mv ./kops /usr/local/bin/
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops export kubecfg --admin
wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml -O metrics-server-components.yaml
kubectl apply -f metrics-server-components.yaml
kubectl get deployment metrics-server -n kube-system
kubectl create ns appdynamics
helm repo add appdynamics-charts https://ciscodevnet.github.io/appdynamics-charts
#The put to vault needs to be done once, do not include yaml in this dir!
#vault kv put concourse/cisco-fso-labs/appd-helm-values data=$(base64 < values.yaml)
vault kv get -field data concourse/cisco-fso-labs/appd-helm-values | base64 -d > values.yaml
mkdir ~/.kube
#get the lab cluster kube-config from the vault.
vault kv get -field data concourse/cisco-fso-labs/lab-kube-config | base64 -d > ~/.kube/config



