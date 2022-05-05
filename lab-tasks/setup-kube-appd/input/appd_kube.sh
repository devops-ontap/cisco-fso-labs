#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
curl -Lo kops https://github.com/kubernetes/kops/releases/download/$(curl -s https://api.github.com/repos/kubernetes/kops/releases/latest | grep tag_name | cut -d '"' -f 4)/kops-linux-amd64
chmod +x ./kops
mv ./kops /usr/local/bin/
#helm repo add appdynamics-charts https://ciscodevnet.github.io/appdynamics-charts
#The put to vault needs to be done once, do not include yaml in this dir! Future - Chart Values can go in vault or be pulled from git on demand(better idea)
#get the appD kube cluster agent config file from vault - it has the account secret in it so its kept in the vault since you cannot change this secret its static
#login to vault
vault login --no-print $SSH_TOKEN
#vault kv get -field data concourse/cisco-fso-labs/appd-helm-values | base64 -d > values.yaml
mkdir ~/.kube
#get the lab cluster kube-config from the vault.
vault kv get -field kubeconfig concourse/cisco-fso-labs/lab-kube-config > ~/.kube/config
chmod 400 ~/.kube/config
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops export kubecfg --admin
kubectl get ns
#wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml -O metrics-server-components.yaml
#kubectl apply -f metrics-server-components.yaml
#kubectl get deployment metrics-server -n kube-system
#Add check if exists skip if not....
#kubectl create ns appdynamics
#helm install -f ./values.yaml appdynamics-1 appdynamics-charts/cluster-agent --namespace=appdynamics



