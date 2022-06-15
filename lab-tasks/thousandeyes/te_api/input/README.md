Lab Prep - Watch this video (15 min)
Webex meeting recording: Automation - Programmatically Auth to FSO APIs
Password: gQSPhrT9
Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=6c4ca1edec6eafe4f3e88b9e57961a2f

Understand that the Instructor has already generated an API key from the GUI and entered it into the vault.
You must logon to the GUI with an account admin to add in other accouns and grant them the account owner rights which will
permit them to authenticate via the API.


After the Instructor Demonstrates and explains this task, please proceed to execute the task yourself.

To run this task, make sure you are in the input directory:
$cd cisco-fso-labs/lab-tasks/thousandeyes/te_api/input

Login via fly with the username and password assigned to you by your Lab Instructor
$fly --target=cisco-fso-labs login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs --username=username --password="password"

Run the task and verify you can authenticate to and get a valid json response from the AppD API:
$fly -t cisco-fso-labs e -c te_api_task_vault.yml

This task is getting the TE_OATHTOKEN value from vault, using it to authenticate to the Thousand Eyes API, then it is 
querying the API for a list of Enteprise Agent IDS. It returns this list to us as we require it to provision a new test and add
our list of agents to the new test we create.

$fly -t cisco-fso-labs e -c te_api_task_vault.yml
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

Related Reading..
API Create Tests:
https://www.thousandeyes.com/blog/automating-test-creation-with-thousandeyes-api/

After running script to get the AgentIDs into a list and or vars, ingest that list
into creating the tests

Get Tests:
curl https://api.thousandeyes.com/v6/tests.json \

Get Agents:
curl https://api.thousandeyes.com/v6/agents.json \
--header "Authorization: Bearer token"

curl https://api.thousandeyes.com/v6/agents.json \
-u token


Further Material on Thousand Eyes Tests
=======================================
ANOJ MODI Recording on how to create Network Tests and Details around how the tests work:
https://salesconnect.cloudapps.cisco.com/vid/index.html?cid=95f4fd1d-b4eb-4208-ab00-c7a48ee22cd3

Install the Thousand Eyes Enterprise Agent

After installing the Agent, immediately after you will want to get the AgentIds
And all other variables related to the Agents so that you can set up the tests


How to install agents manually if automation is not of interest to you and how to troubleshoot Agents manually..
==================================================================================================================
curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
chmod +x install_thousandeyes.sh
sudo ./install_thousandeyes.sh -f -b token

Login to TE and check Agent shows up
https://app.thousandeyes.com/login

How to Stop, Start, Restart Agent and View Logs.

Check status:
service te-agent status

Stop:
sudo service te-agent stop

Start:
sudo service te-agent start

remote the agent:
sudo apt-get -y purge te-agent

Config File:
-/etc/te-agent.cfg


ps -u -p 102600
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      102600  0.2  0.7 1381504 30324 ?       Ssl  21:11   0:00 /usr/local/bin/te-agent -C /etc/te-agent.cfg
ubuntu@ip-10-10-10-236:~$

ps -u -p 113703
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root      113703  0.0  0.7 611048 28184 ?        Ssl  21:21   0:00 /usr/local/bin/te-agent -C /etc/te-agent.cfg


https://developer.thousandeyes.com/v6/

Get Token from GUI - Accounts Section





Manual One Offs.....
Replace your token in the commands below

Create API Token via GUI
oAuth
--header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441" - fsolab4


curl https://api.thousandeyes.com/v6/agents --header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"

Get Agents:
curl https://api.thousandeyes.com/v6/agents.json \
--header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"

Get Usage and Cost:
curl https://api.thousandeyes.com/v6/usage.json \
--header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"


Setup Tests via API
Get Your AgentID

curl -i https://api.thousandeyes.com/v6/instant/agent-to-server \
-d '{ "agents": [ {"agentId": 443531} ], "testName": "agent-to-server-test-443531", "server": "www.thousandeyes.com" }' \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
--header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"


Basic
z4eylr86cwzk1wb5gwp51a805s7wv062
curl -i https://api.thousandeyes.com/v6/status -u noreply@thousandeyes.com:z4eylr86cwzk1wb5gwp51a805s7wv062



Helpful Links on working with Json..
https://stackoverflow.com/questions/29051573/python-filter-list-of-dictionaries-based-on-key-value
https://www.geeksforgeeks.org/python-convert-a-list-to-dictionary/

