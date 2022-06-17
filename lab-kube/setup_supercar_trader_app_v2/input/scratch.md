put the lb svc to var
example:

MYSQL_LB=$(kubectl get svc --namespace supercar-trader mysql -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')



kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.29-debian-11-r3 --namespace supercar-trader --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash
mysql -h mysql.supercar-trader.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD"
mysql -h aa0bd6b2df6e9843f5ae327474004a94e-1118201487.us-east-2.elb.amazonaws.com:3306 -uroot -p"$MYSQL_ROOT_PASSWORD"



kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.29-debian-11-r3 --namespace supercar-trader --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash -c "mysql -h mysql.supercar-trader.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD" <         
-- /bin/bash -c "