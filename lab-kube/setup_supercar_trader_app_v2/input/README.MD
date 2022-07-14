The pipeline is set under main but can be run by cisco-fso-labs

Make sure to authenticate to the team cisco-fso-labs to run task...due to vault..

After deployment - the app will show up at the load balancer URL with:

/.do


Custom Docker Image from Centos 7 and Tomcat 8 installed:

When building the docker image - in order to systemctl you must launch container like this...

This works..
docker run -d -t --name centos --cap-add=NET_ADMIN -h centos:7 --privileged=true centos /usr/sbin/init


Notes:
In pipeline created an oci build of centos7 with tomcat 8.
Stopped catalina copied up some custom config files
started catalina
Also this container has a git pull of the supercar trader app...
fire up container and see where it dumpted the git clone
Add into the sh file to get into that directory
Deploy the msql helm chart and then deploy the app
May in fact not need the lb for msql




how to install tomcat
https://www.digitalocean.com/community/tutorials/how-to-install-apache-tomcat-8-on-centos-7


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

#Will need to write this to the vault


kubectl run mysql-client --rm --tty -i --restart='Never' --image  docker.io/bitnami/mysql:8.0.29-debian-11-r3 --namespace supercar-trader --env MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD --command -- bash

mysql -h mysql.supercar-trader.svc.cluster.local -uroot -p"$MYSQL_ROOT_PASSWORD"

#Figure out how to exist the prompt

