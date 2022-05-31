To Install the TE Ent Agents on your list of IPs - add the IPs to the hostsfile
When your Pipeline Deployed your environment to AWS, it wrote an SSH Key to the vault.
This will be used for the SSH operations the pipeline and tasks perform against any EC2 instances to install agents.


execute the task as follows:
fly -t ci e -c configure_te_agents_task.yml

What is happening?
- The task pulls the appropriate docker images to generate the build container in concourse,
- loads the git repo and branch
- executes the task which calls the shell script to prepare the container further with python modules required etc.
- executes the python script which loops through the list of agents in the hostfile and runs the commandfile on each agent to install the TE Agent.

This task will install the TE Enterprise Agent on all IPs in the hostfile

To remove the agents, you can run the removal task but you will also need to make an API call to blow them out of TE 