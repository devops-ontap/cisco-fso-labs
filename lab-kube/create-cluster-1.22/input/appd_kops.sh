#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x ./kops
mv ./kops /usr/local/bin/
export NAME=lab-kube.k8s.local
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops create cluster --zones=us-east-2a ${NAME}
kops update cluster ${NAME} --yes
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops export kubecfg --admin
#Need to get the kubeconfig file to yaml and then write it to the vault so in the subsequent tasks it can be called from the vault.....
vault login --no-print $SSH_TOKEN
cp ~/.kube/config .
#delete the secret from the vault before re-creating it...
vault kv put concourse/cisco-fso-labs/lab-kube-config kubeconfig=@config
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml


