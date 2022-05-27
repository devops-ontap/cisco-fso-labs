Student Lab Day 1 Prep
===================
Day 1 Overview - See Power Point Slide Day 1 Students
Today you will ensure you have installed the pre-requs for this lab:
IDE
git
fly
jupyter notebook


Preparation - This can be one the day in advance. Most Students will already have these tools installed except for Jupyter.
Jupyter is only required if you do not already have a tool  installed that you enjoy working with for test writing python.
===================

Install Fly
================
(See How_To_Install_Fly.md)

Install Git
=============
(https://github.com/git-guides/install-git)


Install Jupyter Notebook 
========================
https://jupyter.org/install

Install Python 3.x if you do not already have it installed
==========================================================
https://www.python.org/downloads/


Create a Directory on your local machine in which you will maintain all your lab work
=====================================================================================
example:
#sudo mkdir mylab
#cd mylab

Create another directory:
(this directory is for items we do NOT want to push to the git repo)
#sudo mkdir params

Checkout Lab Repo:
==================
https://github.com/devops-ontap/cisco-fso-labs

Checkout Your Assigned Branch and change into its directory
(Instructor will assign each student a branch - checkout your branch)
#git checkout yourbranch
#cd cisco-fso-labs
#git fetch --all

Double-Check/Verify you are in the correct branch
#git status

Logon to Thousand Eyes
========================
https://app.thousandeyes.com
(Invitation will have been received in email day before or morning of lab)

Logon to Concourse via the CLI:
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






 


