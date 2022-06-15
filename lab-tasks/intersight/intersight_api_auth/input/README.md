Lab Prep - Watch this video (15 min)
Webex meeting recording: Automation - Programmatically Auth to FSO APIs
Password: gQSPhrT9
Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=6c4ca1edec6eafe4f3e88b9e57961a2f

Understand that the Instructor has already generated an API key from the GUI and entered it into the vault.

To run this task, make sure you are in the input directory:
$cd cisco-fso-labs/lab-tasks/intersight/intersight_api_auth/input

Login via fly with the username and password assigned to you by your Lab Instructor
$fly --target=cisco-fso-labs login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs --username=username --password="password"

Run the task and verify you can authenticate to and get a valid json response from the Intersight API:
$fly -t cisco-fso-labs e -c Intersight-task.yml

What happens?
 - the task first instructs the Concourse CI to deploy an ephemeral build container using the docker image specified in the task yaml file.
(the build container is deployed from a docker image that is curated to have all libraries, modules, etc installed to operate with the API)
 - the Concouse CI is integrated with Vault in the backend, so that the variable values including the API token and SSH key are passed into the build container 
as environmental variables so they can be utilized by python code
 - the input directory is copied up to the build container
 - the commands in the task yaml are executed on the build container
 - the commands execute against the api and return the requested json data - in this case our output is a list of devices returned by the  intersight api
 - if successful, the build container disappears - it is garbage collected.

You provided code input, it was processed in an ephemeral build container, now you have the output to do with what you like.
In the next task the instructor will show you python tequniques for getting the specific key value pairs or just values you want from the json data
in order to use it as input in later tasks or in your pipeline.

In this lab, we use vault not only for our tokens, api keys, rsa keys, passwords, but also for config files, CIDR ranges and as a general artifactory
for anything that is output we want to retain so we can lifecyle that in the future or utilize it as a input.

If you want to run these python scripts in your own environment on their own or call them from your own CI tool you can easily as they
are completely variablized and paramaterized.




Related Readings....
https://github.com/ciscodevnet/intersight-python

Intersight Labs:
https://developer.cisco.com/site/intersight/

Youtube Videos/Channel:
https://www.youtube.com/playlist?list=PLIlKAL_0d4EwXOuVnIvvJuh-dU-t47CaT

Terraform Lab:
https://devnetsandbox.cisco.com/RM/Diagram/Index/daad55dd-45f1-46c6-a1b4-7339b318c970?diagramType=Topology


The Intersight API Auth using Python Requests is borrowed from here:
Requests Module Auth
https://github.com/briamorr/IntersightDeviceContractStatus/blob/main/contractstatus.py

Postman Collection for Intersight
==================================
https://github.com/CiscoDevNet/intersight-postman

