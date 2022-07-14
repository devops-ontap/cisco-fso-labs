Sonar Chart:

https://github.com/SonarSource/helm-chart-sonarqube/tree/master/charts/sonarqube

Changes to Values.yaml
Enabled Ingress 
Change ClusterIp to LoadBalancer
Set Hostname to sonarqube.devops-ontap.com
Added route53 DNS to the LB that is provisioned as a service to the namespace

login
admin


