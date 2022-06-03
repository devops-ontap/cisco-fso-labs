Deploy Centos 7 to kubernetes....or on EC2
Download the Java APM Agent - use API

The controller-info.xml here is for reference and training purposes to show students what the unconfigured file
looks like

The configured file resides in the vault


If Manual Steps Preferred by Student...
Downloading Agent....
example...for sun rockit
curl -L -O -H "Authorization: Bearer eyJraWQiOiJLRUpyaXk5V21PRVROVzlONF9mQnE2bE5WQ3A0UVBfNHdWS0V2RlR4dUJ3IiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkVxWDdlZ3JEZFdoTmh3TWowOV9BaDRmcUw0Y0QyWFVmc3diemRyaGJzaGcub2FyMWR0ejcxbWRGdEFiVVgycDciLCJpc3MiOiJodHRwczovL2FwcGQtaWRlbnRpdHkub2t0YS5jb20vb2F1dGgyL2F1c3B2bnAzdmtrclNIMk9RMnA2IiwiYXVkIjoibWljb3JzZXJ2aWNlcyIsImlhdCI6MTY1MTI2MTQ4OSwiZXhwIjoxNjUxMzQ3ODg5LCJjaWQiOiIwb2ExanMxMHQ3ekJjTENnRzJwNyIsInVpZCI6IjAwdWVleDBpZ3VORkppcjYwMnA3Iiwic2NwIjpbIm9wZW5pZCIsIm9mZmxpbmVfYWNjZXNzIiwiZG93bmxvYWQiXSwiYXV0aF90aW1lIjoxNjUxMjYxNDM0LCJzdWIiOiJzY29ucm9kQGNpc2NvLmNvbSJ9.R4LW6XO_NdijEIXbdOmxjPpqTb6heG-Ir5VsVb-H7LehDKlhl_aK-lO3plaR1jSFVsZSWPvY_NV10s-VTAnZeKgOZ79_2dd5G1Op1V9dzeFuA0Dv7Vt59h_OCZpPYc1kRQtDkVZRLl63Gu8hfBbx8FZWT7TPPeQZpfFpdSSTKuB5PCYEwYMufs89PfjV5K1qArgqsTo8HXGcv60m-ONzo0Qn6kI_45pOi3VIh4CMAicSjqUAYnkDWmyGTBjgcrzAOMbSSmvJSVvReZSjD23wcsccM4DkTfdcURKOeXRaXJkij-_ELYnur9mwAWF-SIt2dJwtYsYr-OkMWAKHYZZ8Wg;" "https://download.appdynamics.com/download/prox/download-file/sun-jvm/22.4.0.33722/AppServerAgent-22.4.0.33722.zip"

cd /opt
sudo mkdir appdynamics
sudo chown -R centos:centos /opt/appdynamics
cd /opt/appdynamics
mkdir javaagent

unzip into the javaagent directory

in the /opt/appdynamics/javaagent/ver22.4.0.33722/conf is the controller-info.xml which you need to keep in the vault.....
Show students what it looks like when its not customized.
Pushed the customized version to the vault in base 64 or not...for lab maybe not...


Done in Advance by Instructor..
vault kv put concourse/cisco-fso-labs/appd-controller-info data=$(base64 < /Users/sconrod/API-Trainings/dev/ARCH/cisco-fso-labs/controller-info.xml)


Manual Steps if you like....

curl down the apm agent installer.......remember to get and use token python module
curl -L -O -H "Authorization: Bearer eyJraWQiOiJLRUpyaXk5V21PRVROVzlONF9mQnE2bE5WQ3A0UVBfNHdWS0V2RlR4dUJ3IiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkVxWDdlZ3JEZFdoTmh3TWowOV9BaDRmcUw0Y0QyWFVmc3diemRyaGJzaGcub2FyMWR0ejcxbWRGdEFiVVgycDciLCJpc3MiOiJodHRwczovL2FwcGQtaWRlbnRpdHkub2t0YS5jb20vb2F1dGgyL2F1c3B2bnAzdmtrclNIMk9RMnA2IiwiYXVkIjoibWljb3JzZXJ2aWNlcyIsImlhdCI6MTY1MTI2MTQ4OSwiZXhwIjoxNjUxMzQ3ODg5LCJjaWQiOiIwb2ExanMxMHQ3ekJjTENnRzJwNyIsInVpZCI6IjAwdWVleDBpZ3VORkppcjYwMnA3Iiwic2NwIjpbIm9wZW5pZCIsIm9mZmxpbmVfYWNjZXNzIiwiZG93bmxvYWQiXSwiYXV0aF90aW1lIjoxNjUxMjYxNDM0LCJzdWIiOiJzY29ucm9kQGNpc2NvLmNvbSJ9.R4LW6XO_NdijEIXbdOmxjPpqTb6heG-Ir5VsVb-H7LehDKlhl_aK-lO3plaR1jSFVsZSWPvY_NV10s-VTAnZeKgOZ79_2dd5G1Op1V9dzeFuA0Dv7Vt59h_OCZpPYc1kRQtDkVZRLl63Gu8hfBbx8FZWT7TPPeQZpfFpdSSTKuB5PCYEwYMufs89PfjV5K1qArgqsTo8HXGcv60m-ONzo0Qn6kI_45pOi3VIh4CMAicSjqUAYnkDWmyGTBjgcrzAOMbSSmvJSVvReZSjD23wcsccM4DkTfdcURKOeXRaXJkij-_ELYnur9mwAWF-SIt2dJwtYsYr-OkMWAKHYZZ8Wg;" "https://download.appdynamics.com/download/prox/download-file/sun-jvm/22.4.0.33722/AppServerAgent-22.4.0.33722.zip"


cd /opt
sudo mkdir appdynamics
sudo chown -R centos:centos /opt/appdynamics
cd /opt/appdynamics
mkdir javaagent
cd cd /opt/appdynamics/javaagent
unzip *.zip

Prepare the controller-info.xml file in advance and save to the vault.....
example......
vault kv put concourse/cisco-fso-labs/appd-controller-info data=$(base64 < /Users/sconrod/API-Trainings/dev/ARCH/cisco-fso-labs/controller-info.xml)

Now any code calling this will call....

Get the controller-info.xml file out of the vault
vault kv get -field data concourse/cisco-fso-labs/appd-controller-info | base64 -d > /opt/appdynamics/javaagent/ver22.4.0.33722/conf/controller-info.xml

These fields have been customized and the file pushed to the vault already to save time in the lab.....
controller-host
controller-port
controller-ssl-enabled
application-name
tier-name
node-name
account-name
account-access-key

Apache Tomcat should be installed on the centos7 container
(Deploy in Advance)
sudo systemctl stop apache-tomcat-7.service
update the tomcat startup file..
cd /usr/local/apache/apache-tomcat-7/bin
(for now just exec onto the pod..but if pod respins in trouble...so...)
Need to install git on the pod....

Create a custom Docker image - which is tomcat plus the WAR file 



Add this line after line 111 in the catalina.sh file:
Set this on the pre-build docker container..
export CATALINA_OPTS="$CATALINA_OPTS -javaagent:/opt/appdynamics/javaagent/javaagent.jar"
sudo systemctl start apache-tomcat-7.service
sudo netstat -tulpn | grep LISTEN

cd /opt/appdynamics
git clone https://github.com/Appdynamics/DevNet-Labs.git

Create a service in kubernetes to expose the tomcat application externally...

http://IP_OF_APPLICATION_VM:8080

Click Manage App
login with:
Username: admin
Password: welcome1

You should now see the Tomcat Manager App page.

Enter /Supercar-Trader in the Context Path (required): field.

Enter the following path in the WAR or Directory path: field.

file://opt/appdynamics/DevNet-Labs/applications/Supercar-Trader/Supercar-Trader.war

The sample application home page is accessible through your web browser with a URL in the format http://IP_OF_APPLICATION_VM:8080/Supercar-Trader/home.do. Enter that URL in your browser's navigation bar, substituting the IP Address of your Application VM.

Start the load generation for the sample application
Initiate the transaction load for the application using the commands below.

sudo chmod 754 /opt/appdynamics/DevNet-Labs/applications/Load-Generator/phantomjs/*.sh

cd /opt/appdynamics/DevNet-Labs/applications/Load-Generator/phantomjs

./start_load.sh


Installing Tomcat helm chart...into tomcat ns
helm repo add bitnami https://charts.bitnami.com/bitnami
kubectl get svc --namespace tomcat -w tomcat
It is preset to use an external load balancer....
Update the Route 53 DNS or just use the service maybe....??

Create automation job to update route 53 with cname records....

Created a Custom Docker Container with tomcat and with the git repo added for the racer app...
sconrod/tomcat:1.0
(Did not install the APM Agent given its a docker container)

If doing this for an EC2 image then you can create an custom IAM with it installed....

Create a kubernetes deployment manifest...






















