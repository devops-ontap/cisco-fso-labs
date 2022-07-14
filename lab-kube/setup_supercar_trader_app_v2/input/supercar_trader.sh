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
vault login --no-print $SSH_TOKEN
mkdir ~/.kube
vault kv get -field kubeconfig concourse/cisco-fso-labs/lab-kube-config > ~/.kube/config
kubectl create ns supercar
#vault kv get -field data concourse/cisco-fso-labs/supercar-values | base64 -d > values.yaml
kubectl -n supercar delete deploy --all
helm -n supercar delete mysql
kubectl -n supercar delete pvc --all
kubectl -n supercar delete svc tomcat-lb
kubectl -n supercar delete mysql-lb
kubectl -n supercar apply -f supercar-trader.yml
kubectl -n supercar apply -f tomcat_lb.yml
kubectl -n supercar get svc
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install -n supercar mysql bitnami/mysql -f mysql-values.yaml
MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace supercar mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)
echo $MYSQL_ROOT_PASSWORD
apt -y update
apt -y install mysql-client
git clone https://github.com/sherifadel90/AppDynamics-SupercarsJavaApp.git
echo "waiting for mysql loadBalancer to be provisioned in AWS....."
sleep 3m
MYSQL_LB=$(kubectl get svc --namespace supercar mysql -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
cd AppDynamics-SupercarsJavaApp/supercar/src/main/resources/db
mysql -h $MYSQL_LB -uroot -p"$MYSQL_ROOT_PASSWORD" < mysql-01.sql --force







