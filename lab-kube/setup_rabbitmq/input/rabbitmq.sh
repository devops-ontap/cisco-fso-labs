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
kubectl create ns rabbitmq
helm repo add bitnami https://charts.bitnami.com/bitnami
helm -n rabbitmq delete rabbitmq
kubectl -n rabbitmq delete pvc --all
helm -n rabbitmq install rabbitmq bitnami/rabbitmq -f values.yaml
echo "Waiting for AWS to provision loadBalancer........3 min..."
sleep 3m
export SERVICE_IP=$(kubectl get svc --namespace rabbitmq rabbitmq --template "{{ range (index .status.loadBalancer.ingress 0) }}{{ . }}{{ end }}")
echo "To Access the RabbitMQ AMQP port:"
echo "URL : amqp://$SERVICE_IP:5672/"
To Access the RabbitMQ Management interface:
echo "URL : http://$SERVICE_IP:15672/"











