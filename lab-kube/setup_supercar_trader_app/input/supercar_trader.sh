#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops export kubecfg --admin
vault login --no-print $SSH_TOKEN
mkdir ~/.kube
vault kv get -field kubeconfig concourse/cisco-fso-labs/lab-kube-config > ~/.kube/config
kubectl create ns supercar-trader
#vault kv get -field data concourse/cisco-fso-labs/supercar-trader-values | base64 -d > values.yaml
kubectl -n supercar-trader delete deploy
kubectl -n supercar-trader apply -f supercar-trader.yml
kubectl -n supercar-trader apply -f tomcat_lb.yml
kubectl -n supercar-trader get svc -w
