Instructors/Lab Admins Activity Only



After completing the AppD module for the AppD kube cluster and Speed Car Racer Kube deployment - delete the entire cluster
Kubernetes clusters are expensive and we do not need to run this cluster all the time, only when performing specific 
work in the lab.

To DELETE THE LAB KUBE CLUSTER:

change into the directory:
$cd cisco-fso-labs/lab-kube/delete-cluster-1.22/input

run the task:
$fly -t cisco-fso-labs e -c appd_DELETE_kops_task.yml -v aws.region=us-east-2 -v az.name=us-east-2a

View the task output to verify there are no errors. It takes approximately 5 minutes for the cluster and all of its
objects to clear out of AWS.

To Do:
Move this pipeline to the CI Admin user profile only so Students cannot accidentally delete or create more clusters.
It was the original plan to allow each student to have their own cluster, but later it was determined that was overkill
and indeed since this is an API lab we can used one shared kubernetes cluster to perform the AppD api training for the 
AppD kube cluster agent use case of the lab tasks

When you have completed the lab instruction that pertains to this cluster delete the entire cluster as follows:

