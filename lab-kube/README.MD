Instructors/Lab Admins Only:

Immediately prior to starting the AppD Use Case Modules in the lab, spin up the lab kube cluster 
We spin it up on demand when we use it and remove it when done so as not to be incurring extra cost when it is not in use.

deploy-kube-iam-pipeline.yml 

This pipeline needs to be transitioned into a task and doesn't need to be an entire pipeline since there is no python code it is only a shell script

However, for now this pipeline only needs to be run once - it sets up the IAM account, roles, etc
that will be written to the vault and used to deploy the kube cluster used for the AppDynamics 3 main use cases:
AppD Kube Cluster Agent
AppD Kube Deploy of Java App Agent

Once the kube cluster is deployed, and the kube config file is written to the vault, you can interact with kubectl by
spinning up the ephemeral build container and then intercept it to run kubectl commands




