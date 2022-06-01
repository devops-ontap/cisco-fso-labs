#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops export kubecfg --admin
#Install kubernetes metrics server into default namespace
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
helm repo add appdynamics-charts https://ciscodevnet.github.io/appdynamics-charts
#vault kv put concourse/cisco-fso-labs/appd-helm-values data=$(base64 < values.yaml)
vault login --no-print $SSH_TOKEN
mkdir ~/.kube
vault kv get -field kubeconfig concourse/cisco-fso-labs/lab-kube-config > ~/.kube/config
kubectl create ns appdynamics
vault kv get -field data concourse/cisco-fso-labs/appd-helm-values | base64 -d > values.yaml
helm install -f ./values.yaml appdynamics appdynamics-charts/cluster-agent --namespace=appdynamics
helm -n appdynamics ls

