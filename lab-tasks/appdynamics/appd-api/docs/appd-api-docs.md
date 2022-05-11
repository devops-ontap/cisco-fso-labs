Getting Started
==================


To Prepare this lab for you we have done the following steps already, so you do not need to perform these.
We are simply explaining so that when you return home to your own lab or environment you will know how to perform 
these prep steps to your own vault or password safe.

Self Paced:
============
* Watch the Video Here for a high level overview:
* Webex meeting recording: AppD API Auth Kickstart - Vault Integration via OCI Build Container
* Password: cRUZpCJ6
* Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=670a35e97ba392bb7567f0e5e37f11b1



#DO NOT DO THESE STEPS, THEY HAVE BEEN DONE ALREADY FOR YOU, THEY ARE ONLY DOCUMENTED HERE FOR POSTERITY!
* Logon to the lab account as an Account Owner
* Select the Gear Icon in the top right corner
* Select Administration
* Select the API Client TAb
* selected our lab account, and granted it the "Account Owner" role
* select generate secret, copy the secret and enter it into the vault OR if you are just running an initial test paste the secret into your code.
* select the save button on the far right 
* saved this secret and value to our vault

DO THESE STEPS BELOW:
=====================
#Explanation
Since our Vault is integrated with Concourse CI, when you launch a code building task - the ephemeral oci build container container(built from a docker file), has the 
ability to read/write from vault. Therefore, your AppD tasks, will via python calls to the vault, use the AppD secret to generate a temporary OATH token which is written to the vault.
Every time you launch a task, this process is repeated so each API call a new token is being generated.

Therefore, you can concentrate and focus on writing code that does work against the API and not have to worry about authenticating.
Just import the python3 appd_auth.py module into your python scripts.

Activity #1:
==============
We will combine two separate modules to create your first python module, which will automate authentication to the appd api so moving forward,
all you will need to do is import this module into your python scripts, and the authentication will be automated so you can concentrate and focus on 
learning how to develop useful bulk operations code to the AppD api.

First lets run to separate tasks so we fully understand how the API authentication to appd works. After we step through this, you will
consolidate these two steps into one, and create your first python module that consolidates both tasks into one and automates all authentication going 
forward.

Change into the task directory:
$cd cisco-fso-labs/lab-tasks/appdynamics/appd-api/auth/input

This task, will generate an OCI ephemeral build container. Concourse will authenticate to vault, and then use the appd api secret 
that is recorded in the vault to generate an ephemeral OATH bearer token, and then write that token to the vault.

$fly -t cisco-fso-labs e -c appd_get_token_task.yml

This task, no longer uses the appd secret, it simply calls the vault appd oath secret and passes the value into the container 
as an environmental variable. Python calls that variable and uses it to 'do work' agains the API. Our first API is to query the list of the latest beta agent versions.
Our code will return a list of the latest beta agents in json format. We will then spend sometime and analyze the format of this json and see how we can play around with and manipulate this
json in order to use the output as input to subsequent api calls.


$fly -t cisco-fso-labs e -c appd_use_token_task.yml

Now we will take a quick break from writing code in automation tasks, and use the Jupyter Notebook to learn some advanced 
python json manipulation techniques - that may be useful for you in developing further code to the appd api.

Challenge:
==========

Combine Activity #1, task #1 and task#2 into one task
Hint*This requires you to consolidate or crunch two python scripts into one and create a new task and shell script
to call your new python script.

Test your script out and verify it works. 

If it works, commit the code to your repo 

$git add .
$git commit "created appd consolidated auth module in python & tested in code build task"
$git push

The Solution will be provided the following morning into main branch.
When you arrive in the moring, pull any new changes from main into your branch.
Check the solution. Use your IDE to compare the files side by side so you can see the difference.


You can work on this after the lab completes at your own pace should the time alloted in the live
lab be insufficient.

Activity #2
===============

Explanation:
============

Now that we can automate our authentication to the Thousand Eyes API, and we have a working python script that successfully returns API Data
in json format, go ahead and select 3 API calls of your choice from the AppDynamics API online documentation and add in a new python script to perform 
the desired work against the APIs of your choice!

Select any API from this link and use it in your code:
https://docs.appdynamics.com/21.7/en/extend-appdynamics/appdynamics-apis



Don't be afraid to make mistakes
======================================
The worst that will happen is your code will fail and you will get an error. 
Failure is good actually when writing code, so it is actually desireable to fail the first time to try. 
When you fail you learn.

Even if you have to try random ad hoc thing, just go for it! Your are building code in a safe learning environment. 

You can perform this task in multiple ways so use your creativity and innovative ideas.

One way, would be to use the same task and just add in another python script/module.

Another way, would be to create a bran new task, import the auth module we created in Activity #1.

a third way, would be to rename your input directory to input.bak, then copy it and name the new directory "input", then modify the names of the task, 
shell script, python file. Update the URL in the python file to call the API you have chosen


*****Remember it's Ok to build the code as many times as you like until it works**********
******Ephemeral build containers are garbage collected after use and cost almost nothing to operate so build as many as you like*******

After completion of Activity #2 we will not use our Jupyter Notebook to analyze some more json output, modify it and then
pass specific values into subsequent automation tasks.

Your Instructor will demonstrate.....


#Activity #3
In this activity, we will analyze the json response, determin which key values we need to use as input in subsequent API calls and automate this via a task.
Please wait until we have completed the advanced json primer before starting this section.
In the Advanced json primer ~ we will go over the required skills you will need via python to extract specific output from API json and use it as input to perform bulk operations.



HANDY Links:
=========

https://docs.appdynamics.com/21.6/en/extend-appdynamics/appdynamics-apis/api-clients




