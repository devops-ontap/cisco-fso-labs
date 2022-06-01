Instructors
============

This task installs the AppDynamics Cluster Agent via a helm chart to the lab kube cluster
https://docs.appdynamics.com/22.3/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/install-the-cluster-agent/install-the-cluster-agent-with-helm-charts

Change into the task directory:
$cisco-fso-labs/lab-kube/setup-helm-appd/input

Run the task:
$fly -t cisco-fso-labs e -c appd_kube_task.yml -v aws.region=us-east-2 -v az.name=us-east-2a

Notes:
The helm values.yml file contains our SAS controller account ID and secret so it has been added to the vault with base 64 encoding.
#vault kv put concourse/cisco-fso-labs/appd-helm-values data=$(base64 < values.yaml)

A sample template of what a Partner/Customer would need to fill out in this file is included in this repo for reference.







