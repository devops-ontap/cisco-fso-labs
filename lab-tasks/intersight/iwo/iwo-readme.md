to Do:

Fire up the EC2 instance.
Verify connectivity to the Speed Car Racer App.
Verify how it looks in the GUI
Create an alert in the GUI (pre-cede)
Create an alert via API
Create filter in GUI (pre-cede)
Create Filter in API

Update the main Readme with the hyperlink to the Dockerfiles used to in the tasks to build the oci ephemeral build containers
Create new pipeline and build the intersight oci image

Steps to setup for IWO integration with AppD and TE

Ref:
Cisco AppDynamics, ThousandEyes & Intersight Workload Optimizer Integration Guide


Prep:
At this point, the automation tasks have been completed for Day 1 AppD and TE
Running at this time are:
Lab Kubernetes Cluster which has a Deployment of Speed Car Racer App and SQL DB
The Kube Cluster Agent is installed and visible in AppD
The App Deployment has a Java Agent running in AppD
There is a TE Agent installed in the Same AZ as the Cluster and App(s) as well as mysql DB on helm chart

Students have completed Day 1 for AppDynamics and Thousand Eyes and the Instructor has test generated LOAD
with the Java Load Balancer that is part of the speed car racer app deployment and everyone has used 
GUIs in AppD and also TE to view the load.


for this part of the lab, we have pre-deployed a two node kubernetes cluster to the lab environment that is a shared resource
The cluster already has the App Dynamics Cluster Agent Deployed.
The cluster has a kubernetes deployed of the Speed Car Racer App Deployed, with the Java Agent for AppD embedded.
The cluster has a mysql kubernetes deployment also installed with the AppD Agent.

The Instructor will logon to the AppD Web Console and show the students -
The Students may also logon to the Console to view this.

There is also an EC2 instance with the Spped Car Racer App installed.

Because this lab has an API focus - we will briefly go over how the Agent is installed however, we will not be focusing on the install steps of the AppD Agents
The students will not be performing this install unless they request. There are tasks setup for the install, if students wish to learn about this.

We will be focusing on using the API to set up Alerts and filters for this app.
Then we will use a load testing app to generate load and try to trigger some of the alerts.
Once we have triggered the alerts we will use the API to handle the json responses.



Go Over the steps that were done previously to 1. Install the kube cluster agent for AppD 2. Install the Kube Deploy of Race Car App and AppD Agent
Verify the app is accessible via Internet - there is a svc with an external LB that has a corresponding Route 53 CNAME record - this is currently manual but can be automated
in pipeline in later release.

Deploy the Load Generating Java App and Generate Load.
Simulate an outage but taking down either the service or the DNS or an interface(can use the App instance on the EC2 instance as well) or all three. Observe the changes in AppD and also in TE

Verify the alerts are working....set up alerts for this app (have not done yet) - AppD 
Thousand Eyes

View in IWO and set up action when for example, CPU or RAM hits xyz........








