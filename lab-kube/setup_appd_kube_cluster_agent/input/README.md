Instructors
============

Note: You cannot add two different kube clusters to AppD if they have the same release and namespace names.
This seems to be a bug. Make sure that when you install the kubernetes cluster agent, that you ensure it is installed to
a unique namespace name

This task installs the AppDynamics Cluster Agent via a helm chart to the lab kube cluster
https://docs.appdynamics.com/22.3/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/install-the-cluster-agent/install-the-cluster-agent-with-helm-charts


Watch the 5 min Recording Here:
================================
Webex meeting recording: AppD Cluster Agent Helm Install
Password: dZyJwch2
Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=b9c4f1916b9dc0ddeca3b6c55f49d98d


Change into the task directory:
===============================
$cisco-fso-labs/lab-kube/setup-helm-appd/input

Run the task:
==============
$fly -t cisco-fso-labs e -c appd_helm_task.yml -v aws.region=us-west-2 -v az.name=us-west-2a

Notes:
=======
The helm values.yml file contains our SAS controller account ID and secret so it has been added to the vault with base 64 encoding.
$vault kv put concourse/cisco-fso-labs/appd-helm-values data=$(base64 < values.yaml)

A sample template of what a Partner/Customer would need to fill out in this file is included in this repo for reference.

At this point in time, we are ready to logon to the AppD GUI and observe the kubernetes cluster agent reporting into the console.
Log into the SAS Controller:
https://cisco-apipartnertraininglab.saas.appdynamics.com
Select Servers, Clusters, Select the check box next to the cluster then select Details. 
Instructor will spend some time going over the App D Dashboard for the kube cluster with the Students. See Screen Shot in this dir.

The Instructor can now proceed to deploying the JAVA App running on a tomcat container to the kubecluster and we can observe the 
changes in the AppD GUI.

Move onto the task:

JAVA_APP






