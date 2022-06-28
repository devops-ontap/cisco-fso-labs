Instructor/Lab Admins Only
==========================

It will take about 10 min for the Cluster to be fully deployed into AWS
This is a constraint on how fast AWS can provision

So this message is normal until the cluster is ready...
Validating cluster
W0628 15:52:09.685833      80 validate_cluster.go:184] (will retry): unexpected error during validation: error listing nodes: Get

Cluster must be validated prior to installing Metrics Server Helm Chart & AppD Helm Chart 

To Do: Add into the Test Parallel pipeline the test for the cluster readiness 

example: if cluster validation healthy - do next step in pipeline


Known Issues AppD:
===============
AppD Kubernetes Cluster Agent - Does not register the true Cluster Name in AppD Console.
Instead it registers the namespace where you installed the cluster agent and the release name
This prevents you from installing multiple different kube clusters (each with unique names) if you install
the appD cluster agent into the same namespace name and same release name.

After nuking or completelly deleting or taking offline a kube cluster with the cluster agent installed, AppD
Does not detect the cluster is gone and still reports the PODs as healthy forever.
There is no way to delete the cluster from the Console
It is being investigated if it can be forcibly removed via API

Workaround
===========

Make sure each kubernetes cluster deployment of the AppD Cluster will have a unique release name so it will register in the console.











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
$fly -t cisco-fso-labs e -c appd_kops_task.yml -v aws.region=us-east-2 -v az.name=us-east-2a

You can now proceed to deploy the Helm App D Cluster Agent







