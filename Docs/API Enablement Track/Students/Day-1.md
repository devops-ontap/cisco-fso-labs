Student Lab Day 1 
===================
Preparation - This can be one the day in advance. Most Students will already have these tools installed except for Jupyter.
Jupyter is only required if you do not already have an tool  installed that you enjoy working with for test writing python.
===================

Recommended IDE - Intellij (you can download a 30 day eval)
Not Recommended - Visual Studio (from time to time this IDE will insert white space or special characters into python code)

- [ ] Install Fly
================
(See How_To_Install_Fly.md)

- [ ] Install Git
=============
(https://github.com/git-guides/install-git)


- [ ] Install Jupyter Notebook 
========================
https://jupyter.org/install

- [ ] Install Python 3.x if you do not already have it installed (latest or 3.8)
==========================================================
https://www.python.org/downloads/


- [ ] Create a Directory on your local machine in which you will maintain all your lab work
=====================================================================================
example:
#sudo mkdir mylab
#cd mylab

- [ ] Create another directory:
(this directory is for items we do NOT want to push to the git repo)
#sudo mkdir params

- [ ] Checkout Lab Repo:
==================
change into the mylab directory you created and then clone the repo:
https://github.com/devops-ontap/cisco-fso-labs

- [ ] Checkout Your Assigned Branch and change into its directory
(Instructor will assign each student a branch - checkout your branch)
#git checkout yourbranch
#cd cisco-fso-labs
#git fetch --all

- [ ] Double-Check/Verify you are in the correct branch
#git status


- [ ] Logon to Thousand Eyes - After Instructor Prompt
========================
https://app.thousandeyes.com
(Invitation will have been received in email day before or morning of lab)

- [ ] Logon to App Dynamics Lab GUI - After Instructor Prompt
  ========================
  https://cisco-apipartnertraininglab.saas.appdynamics.com
  (Invitation will have been received in email day before or morning of lab)


- [ ] Logon to Concourse via the CLI:
===============================
(from within your mylab directory.... )
#fly --target=cisco-fso-labs login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs

-You will be prompted to click on an URL
(If not, copy the URL into your Browser)
- Logon with the credentials your lab Instructor provided you
- Copy and Paste the Token back into the CLI
- You are now logged into Concourse
- You will now see your Team in the Browser
- Navigate to Select your Pipeline

If you do not have a Browser, or your Browser is blocked from connecting to the URL you can logon like this......
#fly --target=cisco-fso-labs login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs --username=USERNAME --password=PASSWORD

Verify you can successfully run the following 3 tasks:
==================================================================
These tasks test verify you can auto auth programatically to all three FSO APIs.
Remember - in the instructional video, it states that the API keys for each have already  been entered
into the vault. 


How the Underlying Infrastructure is set up between Concourse and Vault ~Third Party Integration for CICD: Vault and Concourse CI
=========================================================================
When you logged in using fly, based on your username - you are authenticated to a concourse team called cisco-fs-labs.
Concourse has a mount point for cisco-fso-labs in the vault, and when Concourse authenticates to the vault - it can
read/write to that mount point in the vault. 

Each student is assigned a git branch, and the code populates a subdir in the vault for each branch.

When you launch a fly task, it instructs concourse to build an ephemeral code build container from the dockerfile documented in the task, it is able to programatically pass in the required authentication
values to the build container and or python code via an env var fron the vault.

When you run each task, it will authenticate to the respective API and return back a json response. 
The task will also show as "succeeded"

In the next Module, we will running a variety of API Queries, then we will be analzying the json response format from each API and we will
learn some useful Python techniques to pull out from the json responses the specific values we are interested in.

Once we are comfortable with the json responses and how to analyze and get specific values, we will practice passing these values as 
variables into POST actions for each API.

We will also look at how import the data from an API into a database in later modules.


- [ ] 1. Thousand Eyes
Change into this directory:
$cd cisco-fso-labs/lab-tasks/thousandeyes/te_api/input
Run the task:
$fly -t cisco-fso-labs e -c te_api_task_vault.yml

- [ ] 2. AppDynamics
Change into this directory:
$cisco-fso-labs/lab-tasks/appdynamics/appd-api/auth/input
Run these two Tasks:
$fly -t cisco-fso-labs e -c appd_get_token_task.yml
$fly -t cisco-fso-labs e -c appd_use_token_task.yml

- [ ] 3. Intersight
Change into this directory:
$cd cisco-fso-labs/lab-tasks/intersight/intersight_api_auth/input
Run the task:
$fly -t cisco-fso-labs e -c Intersight-task.yml

Review - 
Using automation, you have ran a task that programatically authenticated to each API.

How Did the Task Work?
The task yam file specifies a docker image to pull from docker hub that already has all the libraries and python 
modules installed to communciate with the API

After the task pulls the docker image it builds an ephemeral build container from that image and copies 
up the contents of the input directory from which you launched the task and its contents.

The task then launches the shell script - in the shell script there are vault commands which 
call the vault and pass in the values of the respective authentication token or api key or secret into
the build container as an environmental variable so that the Python script can pull in the values 
to the respective variables in the python script.

Since the container is ephemeral, as soon as the code executes successfully, the container vanishes and is garbage collected.

If you have successfully completed this module please ensure you check all the boxes and git commit and push your branch







 


