#In the morning reconfigure this to write the kubeconfig file to vault in a base64 encoded yaml


This task creates a kops cluster that uses the compatible version of 
kubectl and kops that will work with the AppD Cluster Agent

Only specific versions of kubectl will work with the AppD Cluster Agent
The tasks uses a curated OCI Build container with lastest compatible version of both kubectl and kops to deploy that cluster

Goal is to transition this to run on spot instance for cost savings using SpotInst Ocean

AppD kubernetes cluster agent:
Currently deploying to the following version of AppD and kubectl: 1.22

Branch is kops-kube-1.22(in progress)
Current is 1.22
The pipeline is named 1.21 but need to rename it not to have the version, just check the version in the tag

https://github.com/sconrod-tester/docker-builds/blob/ubuntu-kops/kops-kube-1.22/Dockerfile





