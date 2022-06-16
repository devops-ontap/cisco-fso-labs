Sample Java App:
https://github.com/sherifadel90/AppDynamics-SupercarsJavaApp/blob/master/README.md

After successful deployment - Tomcat will be available via the lb URL

The Supercar-Trader java app will be available at:
lb url/Supercar-Trader/home.do

MYSQL:
helm repo add bitnami https://charts.bitnami.com/bitnami

helm install -n supercar-trader mysql bitnami/mysq

MYSQL_ROOT_PASSWORD=$(kubectl get secret --namespace supercar-trader mysql -o jsonpath="{.data.mysql-root-password}" | base64 -d)

echo $MYSQL_ROOT_PASSWORD
BR5rFkT6qb
#Will need to write this to the vault


kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.29-debian-11-r3 --namespace supercar-trader --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash

mysql -h mysql.supercar-trader.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD"

#Figure out how to exist the prompt

