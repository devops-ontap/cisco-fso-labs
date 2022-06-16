Your Instructor has already set up the following standard use case scenerios to save time and allow you to 
focus on APIs:

AppD Server Agent on EC2 Instance
AppD Java Agent for  Java App on EC2 Instance with 
Kubernetes App D Cluster Agent
Kubernetes App Agent on Java Deployment

Integrations:
AppD Server Agent on TE Agent



Lab Prep - Watch this video (15 min)
Webex meeting recording: Automation - Programmatically Auth to FSO APIs
Password: gQSPhrT9
Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=6c4ca1edec6eafe4f3e88b9e57961a2f

Understand that the Instructor has already generated an API key from the GUI and entered it into the vault.

To run this task, make sure you are in the input directory:
$cd cisco-fso-labs/lab-tasks/appdynamics/appd-api/auth/input

Login via fly with the username and password assigned to you by your Lab Instructor
$fly --target=cisco-fso-labs login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs --username=username --password="password"

Run the task and verify you can authenticate to and get a valid json response from the AppD API:
$fly -t cisco-fso-labs e -c appd_get_token_task.yml
This authenticates to the AppD Api and generates a temporary oath token and writes it to the vault

$fly -t cisco-fso-labs e -c appd_use_token_task.yml
This uses the temp oath token you generated that was written to the vault and uses it to perform an API call that returns json from the AppD API


What happens when you excute a task?
- the task first instructs the Concourse CI to deploy an ephemeral build container using the docker image specified in the task yaml file.
  (the build container is deployed from a docker image that is curated to have all libraries, modules, etc installed to operate with the API)
- the Concouse CI is integrated with Vault in the backend, so that the variable values including the API token and SSH key are passed into the build container
  as environmental variables so they can be utilized by python code
- the input directory is copied up to the build container
- the commands in the task yaml are executed on the build container
- the commands execute against the api and return the requested json data - in this case our output is a list of devices returned by the  AppD api
- if successful, the build container disappears - it is garbage collected.

You provided code input, it was processed in an ephemeral build container, now you have the output to do with what you like.
In the next task the instructor will show you python tequniques for getting the specific key value pairs or just values you want from the json data
in order to use it as input in later tasks or in your pipeline.

In this lab, we use vault not only for our tokens, api keys, rsa keys, passwords, but also for config files, CIDR ranges and as a general artifactory
for anything that is output we want to retain so we can lifecyle that in the future or utilize it as a input.

If you want to run these python scripts in your own environment on their own or call them from your own CI tool you can easily as they
are completely variablized and paramaterized.