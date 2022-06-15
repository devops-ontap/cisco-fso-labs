This task is part of Day 2 Training - Lab Underlying Infrastructure Deployment
=======================================================================================
Prior to Starting this section of the Training, you will have deployed your lab infra via pipeline and you will have a list of
Agent IPs to add to the hostfile.
You will need to commit the hostfile to your branch to deploy agents.

Please wait until the Instructor has demonstrated how to do this.
=====================================================================================================


Tasks in this folder automate the bulk installation of Thousand Eyes Agents onto EC2 Instances
===============================================================================================

Important Note:
====================

Prior to running this task, you must build your infrastructure pipeline. 
It is important to note that :

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