#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
mkdir ~/.kube
vault kv get -field kubeconfig concourse/cisco-fso-labs/lab-kube-config > ~/.kube/config
kubectl create ns iwo-collector
helm install --debug iwo-k8s-collector ./iwok8scollector --namespace iwo-collector --set iwoServerVersion=8.4 --set collectorImage.tag=8.4.4.1 --set targetName=lab-kube.k8s.local


