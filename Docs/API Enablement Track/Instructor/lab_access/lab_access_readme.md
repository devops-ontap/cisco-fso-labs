How to Set up Lab Access - This only needs to be done after a helm upgrade or is recommended after the completion of each lab
============================

Each Lab Student will be granted the Pipeline Operator Role. 
This allows them to run the pipelines but not reconfigure or set the pipelines.

All Students:
========================

- belong to the same Team: cisco-fso-labs

- are granted the "Pipeline Operator" role(This role allows them run pipelines and tasks but not reconfigure, destroy or set pipelines. This ensure stability of the lab env 
while providing the Students with the maximum access to develop code)

Run the following command to set up the Student's access to their Team:
===========================================================================
(This only needs to be done once OR after a helm upgrade of concourse - currently upgrades are done only to scale capacity and will
not be required unless the number of lab users exceeds 20 consecutive. The lab can be scaled via a helm upgrade to accommodate more consecutive student operators)

This command must be run by an Instructor or Lab Admin with the Pipeline Administrator Role, logged into the cisco-fso-labs team:

#fly -t cisco-fso-labs set-team -n cisco-fso-labs -c operator-role-cisco-fso-labs.yml


Currently local access is set up meeaning the Student Accounts are local to concourse. This is intended to change in the next release of the lab.
To reset the Student Account Passwords After the lab, a helm upgrade is done. 

In the next release of the lab, users will either authenticate with git or otka or vault - yet to be decided. Probably it will be vault since vault
is already being used for the lab variable artifactory and credential management. Stay tuned...



