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
kubectl create ns supercar-trader
#vault kv get -field data concourse/cisco-fso-labs/supercar-trader-values | base64 -d > values.yaml
kubectl -n supercar-trader delete deploy --all
helm -n supercar-trader delete mysql
kubectl -n supercar-trader delete pvc --all
kubectl -n supercar-trader delete pv --all
kubectl -n supercar-trader delete svc tomcat-lb
kubectl -n supercar-trader delete mysql-lb
kubectl -n supercar-trader apply -f supercar-trader.yml
kubectl -n supercar-trader apply -f tomcat_lb.yml
kubectl -n supercar-trader get svc
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install -n supercar-trader mysql bitnami/mysql -f mysql-values.yaml
MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace supercar-trader mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)
echo $MYSQL_ROOT_PASSWORD
apt -y update
apt -y install mysql-client
git clone https://github.com/sherifadel90/AppDynamics-SupercarsJavaApp.git
echo "waiting for mysql loadBalancer to be provisioned in AWS....."
sleep 3m
MYSQL_LB=$(kubectl get svc --namespace supercar-trader mysql -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
cd AppDynamics-SupercarsJavaApp/Supercar-Trader/src/main/resources/db
mysql -h $MYSQL_LB -uroot -p"$MYSQL_ROOT_PASSWORD" < mysql-01.sql --force
mysql -h $MYSQL_LB -uroot -p"$MYSQL_ROOT_PASSWORD" < mysql-02.sql --force
mysql -h $MYSQL_LB -uroot -p"$MYSQL_ROOT_PASSWORD" < mysql-03.sql --force






