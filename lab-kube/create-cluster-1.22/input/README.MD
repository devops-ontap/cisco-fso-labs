Instructor/Lab Admins Only
==========================
To Do:
=======
This is a task but will be added into the infra pipeline for the convenience of the Instructor/Lab-Operator
Add step to pipeline to update route-53 with the CNAME record to point to the new load balancer url for the service in the namespace of the app


Instructor/Lab Admin
=======================
Kubernetes Clusters are expensive to operate in AWS so we do not leave this cluster running when it is not in use. We provision it on demand and delete it when done.
It takes approximately 5 minutes to build and 5 minutes to destroy.

Immediately prior to kicking off the lab modules for AppD that use a kube cluster, provision the kube cluster to AWS.

Watch the 5 min video here showing how to run the task to deploy the kube cluster to aws
========================================================================================
Webex meeting recording: Devops - Automate Kubernetes Cluster Deploys to AWS
Password: MrmshGd7
Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=993c4247b9057d6babcec9249f07595f


After provisioning the kube cluster, deploy the Speed Car Racer Deployment - this will deploy a JAVA App and Agent to the kube cluster.
Once the kubernetes load balancer service is up and running, it is required to manually update the route-53 CNAME unless you just give the students the lb url which 
is probably easiest.

To Deploy the kube cluster - this is a self managed cluster. See why Devops prefers self - managed kube clusters as oppossed to managed clusters by watching this
very informative deep dive by Starke and Wayne:
When Managed Kubernetes Isn't: What You Need to Know
https://youtu.be/_oeg1kcfbmY


Change into the directory:
$cd cisco-fso-labs/lab-kube/create-cluster-1.22/input

Run the task:
$cisco-fso-labs/lab-kube/create-cluster-1.22/input/appd_kops_task.yml

You can now proceed to deploy the Helm App D Cluster Agent







