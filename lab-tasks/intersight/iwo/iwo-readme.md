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


In progress:
Go Over the steps that were done previously to 1. Install the kube cluster agent for AppD 2. Install the Kube Deploy of Race Car App and AppD Agent
Verify the app is accessible via Internet - there is a svc with an external LB that has a corresponding Route 53 CNAME record - this is currently manual but can be automated
in pipeline in later release.

Deploy the Load Generating Java App and Generate Load.
Simulate an outage but taking down either the service or the DNS or an interface(can use the App instance on the EC2 instance as well) or all three. Observe the changes in AppD and also in TE

Verify the alerts are working....set up alerts for this app (have not done yet) - AppD 
Thousand Eyes

View in IWO and set up action when for example, CPU or RAM hits xyz........








