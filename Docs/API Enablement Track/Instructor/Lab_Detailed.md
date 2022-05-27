LAB SETUP
=============

Two Paths to Prep Lab.
- For Advanced Devops Engineers, they can deploy their own pipelines and AWS lab Envs.

- For Students new to Devops and Cisco APIS, setup everything in advance so they can hop skip jump to the API development


Students focusing on Developing Code to the Cisco APIS-
In this case the Lab Admin will setup all pipelines in advance.
All Students are working on the same team in concourse: cisco-fso-labs
(this may change to one team per student in the future)
Each Branch has a corresponding Pipeline under the cisco-fso-labs team

***Students MUST authenticate via CLI to concourse*****
This will automatically open their default browser and prompt them to enter credentials.

Instructor Prep
======================
Make sure you have provided Students with following and done the prep one day in advance..
Provide Students with:
- Concourse Logon Name and Password (This is always going to be identical to the branch they are assigned)
- Assigned Git Branch
-Your Assigned Availability Zone(az)
-Add the students email to Thousand Eyes lab - it will send them an email invitation to set their password to Thousand Eyes 
Blitz Lab GUI ENV for which you grant them two roles: standard user, API Admin.
-At Day of Lab verify with everyone they have received this. If not resend invitation via TE Console.

Instructor Setup Steps are in:
==============================
Instructor_Lab_Setup_Prep.md

Student Steps:
==================
Student Detailed Steps for Day are in Day-1.md










Part 1 of this lab demonstrates simple integration with a variety of common APIs that perform standard operational standard stack functions:
vault & artifactory placeholder-
hashicorp vault
kubernetes - ci tool
kubernetes - sample java apps
aws - cloud provider
python, shell, bash
docker
Appdynamics
ThousandEyes
github/gitlab
cisco csr1000v
IOX XE

Part 2 of this lab demonstrates:
Config Management with Terraform Cloud
Automation with Cisco NSO (large managed service providers audience)




Instructors of this lab should have:
Intermediate hands on skills with the following:
git branching and github/gitlab - managing repos and branches, understand git flow and developer processes using git to rapidly iterate on code
advanced json and yaml file format understanding
advanced cisco networking
advanced docker
advanced aws and cloud networking
Advanced knowledge and experience with SDLC, rapid iteration and current develops rapid iteration concepts
Green/Red rapid iteration development cycle and code testing concepts
The importance of ensuring all cloud based infrastructure is managed as code - Infra as Code

Students of this lab require at least basic experience and skills with:
git flow, creating branches, updating code etc.
ssh keys - generating and using
linux command line, shell, bash
basic python
basic docker

Once vetted, the repo will be made public so this is only temporary during the beta testing of the lab




2. Unpause your pipeline, select to deploy the AWS Environment when its complete it will turn green. While it is deploying review the Powerpoint slide which details the architecture and components of the AWS lab environment from a network perspective. Its important to have an understanding of the networking architecture of the lab as we progress through the lab phases.

3. Once the AWS job in the pipeline turns green, you can go ahead and deploy the CSR and the Ubuntu and LAN router instances. These will take some time(about 3 minnutes to build) so during that time you can go ahead and clone the git repo. We are going to configure our CSR using the DEVOPS methodology of rapid iteration in an isolated task (outside the pipeline) to test it then once we are happy with it, we can add it to the pipeline to automate this going forward.

When DEVOPS engineers are working on their code - they work from a branc that typically has a naming convention of username/jira ticket #
In more sophisticated Devops Pipelines such as Microsoft Azure Devops Pipelines, the ticketing system is integrated with both git and the pipeline.
So after an Engineer has tested their code via a task, they will do a build of the pipeline from their branch.
If the build is successful, they will create a PR.
It is worth nothing immediately prior to building, they should ensure they have pulled and merged the latest master branch into their test branch so they are testing against the latest production version of the code.

In this lab, we will not be creating merge requests - however, we will be working like Devops Engineers but building our pipelines from our branch code.

In Later Phases of the Lab, students will be requested to create a PR (Pull Request) that will add in their vetted and tested tasks into the pipeline so these will be automated going forward.

In Large Software Companies, there can be anywhere between 5-100 or more Engineers working on multiple branches on different features or bug requests.

Typically either weekly, bi-weekly, as the business or customer require or on a set release cycle, Engineers will be requested to submit their work by a cut off date and the PRs will be analyzed by two more more Senior Software Leads for a merge into the DEV branch. Once all merges are squashed, the pre-release is build in the DEV branch of the pipeline.

When the DEV branch build is green or passes, it is either automatically or manually promoted to the QA branch where more extensive testing is done.
Typically when the infratructure DEV branch is promoted to QA, it will "initiate" a build of the other 'overlay pipelines'. These are pipelines that deploy the latest production version of the 'bread and butter' business applications on top of the infrastructure. Examples of this are the "Speed Car Racer" java app that we will deploy onto our infrastructure release.

If all our business app pipelines are deployed successfully on top of our QA infra pipeline, we promote our QA to Stage(External Business Customers Test) and then to Production. Typically there are adjacent 'test' pipelines that will run in parallel to run extensive testing against the pipelines. In some cases the tests are simply added in as jobs, and each job will promote only after the test jobs succeed in the pipelines.

Before you can practise 'rapid interation development' on your branch, you need to ensure your SSH key is added to your git account, and you have provided your git account to the lab instructor. The lab Instructor will add you to the repo and you will receive an invite to your email, once you accept you will be able to run the CSR configure task.

On the last day of the lab, we will allow everyone to submit PRs for any tasks we have run manually into their pipeline.
We can then delete their entire lab environment, and build it completely automated end to end from their own newly developed version of their own pipeline.

This is optional and only for individuals passionate about automation and pipelining.




After adding SSH key to git account and receiving invite to the git repo proceed as follows:

1. Clone the git repo
   https://github.com/devops-ontap/cisco-fso-labs

2. Create a Branch - each lab user will create their own branch
- in this lab we will not doing a git merge. people will work from their own branches
- git checkout -b yourbranchname
- git status
- git fetch --all

2. From within your git repo directory - verify your lab_vars.py. You will see the entire lab is deployed using just 5 variables.

3. create a params directory outside of the git repo, and copy out the sample-params.yml file into that directory.
7. Update the params file with your branch name and your SSH private key. You can name the params file by your branch example: us-west-1a.yml
   (This is required for when your run a manual iteration task on your branch because, it will need to authenticate through to the pipeline to allow the pipeline to run the task as a one off).

Once your CSR is deployed you can now practise being a 'DEVOPS Engineer' working on your branch by testing out the CSR Configure task.
This is a one off task that will utilize the pipeline mechanism to launch a 'one off task' that will:

Connect to the Pipeline
Instruct the Pipeline to pull the docker image which netmiko and python installed to create your ephemeral build container
Pull your git branch (using the SSH key specified in the params file) onto the docker build container
Copies your input directory that includes your scripts onto the ephemeral build container
Executes the code on the CSR
If the tasks builds successfully, the task will turn green. If there is an error it will turn red.
The task will provide you with a URL that you can use to view the build progress in your browswer
If the build fails, your ephemeral build container will 'hang out' for several minutes so you can 'hijack' the container to debug.
Typically, hijacking a container is not required. In some cases if our error indicates something to do with connectivity or free space, we would hijack the container to see if we may need to increase our build container size but this is very rare. In this lab, we will not be needing to hijack containers.

To run your task you need need to authenticate via your CLI first as follows:

target the ci tool using fly and set your pipeline
example:
Login to a Team
fly -t ci login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs
This command opens a browser, login and then capture the token and paste it into your command prompt



Detailed Description of what the first step in pipeline automation:
As soon as a git push is done to the branch, the first step in the pipeline
automatically starts. This step:

Grabs the AWS Auth Key from the lastpass vault,
Grabs the resources to be used in the pipeline:
Pulls the docker container and uses it as the pipeline worker container image
Pulls the git branch and dumps it onto the build container
Authenticates to AWS and Creates the SSH key that will be used subsequently to deploy the EC2 images and AWS resources

Start the build of the AWS Env. This will create the resources in the name you set in the vars file:
VPC
Subnets
Route Tables
Routes
Internet Gateway
Security Group
Ingress Rules to allow SSH into lab

Once the Deploy AWS Env job turns green, start the Deploy Cisco CSR1000V job
This job takes the longest, as before much of the code can execute it must wait on the
instance to fully initialize, so there is polling set up in the job.











All configuration in this lab will be done via code in TRUE DEVOPS SPIRIT accept for certain aspects of the Thousand Eyes, AppD and Intersight Setup which is not yet available via API calls.

We will only use the GUI to view the changes we make via code. In reality the GUI is not even required
however, we use it only as a visual familiar representation of our changes as it is most familiar to the students in the lab.

The Instructor and the students will be constantly doing git updates throughout the lab to their branch as the Instructure steps them through the lab
This repetition, will enforce the green/red rapid iteration of code which is an important skill that requires repitition and practise much like playing a musical instrument.

We are not only teaching our students new ways of working with cisco apis, we are teaching them a new modern way of working with network infrastructure as code
in a modern SDLC. This way of working has been used for Software Developers for over 20 years, and by Devops Engineers for over 10 years,  but it is relatively new to Network Administrators.

Traditional on site data centers have established a specific work methodology among the vast population of network administrators - however, due to cloud integrations this way of working no longer can be used
to successfully manage hybrid cloud and cloud networking environments.

To ensure stability of our infrastructure, it is required to manage it via code using the SDLC and Industrial Pipelines.

As soon as a git push is complete, the lab prep job in the pipeline automatically starts




Common Error when trying to SSH to the CSR1000v:
Unable to negotiate with 18.220.247.107 port 22: no matching key exchange method found. Their offer: diffie-hellman-group-exchange-sha1,diffie-hellman-group14-sha1

Add the following to the /etc/ssh/ssh_config
KexAlgorithms diffie-hellman-group1-sha1,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group14-sha1

AWS Ref Docs:
https://docs.aws.amazon.com/cli/latest/reference/ec2/
To see what is possible with an AWS Cli command run this:
aws ec2 create-vpc --generate-cli-skeleton