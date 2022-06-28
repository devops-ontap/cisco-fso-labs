AppD Use Cases:

In this module we will observe three main uses cases for appd and the corresponding API available actions:

1. AppD Java Agent (Shared Lab Resource)
=========================================
An EC2 instance with tomcat and a Java App along with the AppD Java Agent has been pre-created - the EC2 image remains shut off until we start this portion of the lab.
The Instructor will change the state of the Instance via the infra pipeline when ready.
This EC2 instance has a standard tomcat installation and has the Speed Car Racer Java App and AppD agent installed.
The code used to install the Speed Car Racer App is here:
<INSERT LINK TO THE REPO HERE>

The Instructor and Students can view this in the AppD Web Console to start.

Since this lab focuses on the API, we will go over the install steps very quicklly and refer students to the documentation followed
to install the JAVA agent on this app.

2. Kubernetes Cluster Agent (Shared Lab Resource)
=================================================
The Instructor can quickly deploy a two node kubernetes cluster (Share Resource) via the lab infra pipeline - deploy-kube-pipeline.yml
The lab-kube cluster will be deployed to OHIO(us-east-2a)

The kubeconfig file is automatically written to the vault 
When running kubectl, use the kube task to launch an ephemeral build container - then intercept the container and run the kubectl commands if so desired 
The Instructor will quickly perform a kube deployment of the same Speed Car Racer App to the kubernetes cluster along with the load generator app

3.
The Instructor and Students can watch the kube agent appear in the AppD console to start AND they can watch the deployment JAVA app agent appear as well.

Once all agents are successfully registed/showing up in the AppD console, the Instructor will step through setting up one Alert and one Rule to demonstrate to the
lab Students.
The Instructor will then query the API to return the json specs of those objects
The Instructor will then use the API to delete the objects
At this point the Instructor will challenge the students to re-create the objects via the API 

The instructor will then initiate a load against the JAVA app.
the Instructor will show the changes within the AppD console

The Instructor will instigate an outage
Students will verify they see the changes in the console
Students will verify they can see the changes in the JSON data







Prior to commencing this module, the Instructor will via the lab infra pipeline spin up a kube cluster.
The kube cluster
The Instructor or Lab Admin will prepare these steps.