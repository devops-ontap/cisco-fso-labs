Instructors
============

If you or Students want to directly interact with the kube cluster using kubectl simply spin an ephemeral build container and then hijack the container

Change to the directory:
$cd cisco-fso-labs/lab-kube/interact-with-cluster-1.22/input

Run the task to spin the ephemeral build container.....
$fly -t cisco-fso-labs e -c appd_play_kops_task.yml -v aws.region=us-east-2 -v az.name=us-east-2a

Intercept the task Container ....
$fly -t cisco-fso-labs intercept

Now you are on the container, select 3 for the task, and you can run kubectl commands, helm commands etc.
