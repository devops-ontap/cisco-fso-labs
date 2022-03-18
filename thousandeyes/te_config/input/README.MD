To Install the TE Ent Agents on your list of IPs - add the IPs to the hostsfile

Because we are using a pem key to run a task out side of the pipeline,
Copy this directory to your lab-tasks directory outside the repo to test it
from:
cisco-fso-labs/thousand_eyes/te_config/input
to:
lab-tasks/thousand_eyes/te_config/input

from in this directory, copy your pem file and name it key.pem
make the key read only:
chmod 400 key.pem

execute the task as follows:
fly -t ci e -c configure_te_agents_task.yml

The task pulls the appropriate docker images to generate the build container in concourse,
loads the git repo and branch
executes the task which calls the shell script to prepare the container further with python modules required etc.
executes the python script

This task will install the TE Enterprise Agent on all IPs in the hostfile

Remember, if you were simply adding this task into the pipeline, you would not need have the pem key in the directory as the pipeline already has the pem
key.

Another option for the pipeline is to add the pem key to the vault, and  call it via a parameter in the pipeline.