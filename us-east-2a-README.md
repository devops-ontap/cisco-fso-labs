Login to your Team:

Your Team is cisco-fso-labs
There are many people on your team
Anyone in the team and operate any of the other pipelines. Please be careful and respectful and stick to your branch pipeline for the lab duration.

Team are usually made up of Developers working on the same product.
Each Developer can work on their branch - which is set to their own pipeline.
When all Developers are in the 'green', meaning they have tested their own development in their own pipeline, they before creating a PR, pull from main and merge into their branch and test their pipeline again
before submitting a PR.

So you can commit work to your branch as much as you like. If you are happy with it, and it tests out Ok in your pipeline, you can create a PR.
Usually there is a due date which is the end of the sprint which is a 'cut off date', when all the Team must create a PR for their work

The Lead Developers will review the work and if it looks good, and they verify it shows as gree in your branch build, they will merge into the TEST or DEV branch.
On the Due Date, all the Developers will merge in their work.

At this time the Lead Developers will build all the merged changes into the TEST or DEV branch through the TEST or DEV pipeline. If it passes all the tests in the Pipeline it will get promoted to the 
QA pipeline. The QA pipeline is where extensive regression testing happens. It is also where - other higher level QA 'current release' pipelines are 'kicked off' such as web apps for example. 

Typically, before our Teams DEV branch is prompted for the sprint, all the other higher level 'release' versions (that is a copy the code that is currently in production) will all be deployed on top of our DEV pipeline to 
ensure there are no errors.

It is quite common, that DEV will NOT pass, and it gets kicked back for revision sometimes multiple times.

Eventually once all the other Applicatin and Upstream pipelines can be built green on top of our Teams Infra pipeline, we can successfully promote our DEV to QA. Many companies will have a copy of QA which is normally called Staging, into which
thier trusted Customers have access to test out the new pre-release candidate.

If defects are found in Staging...which happens but is rare, the Team can sometimes quickly push a bug fix branch if the fix is simple.
If the defects are too numerous, and 'take down' external custmomer apps, the pre-release can be postponed until all issues are fixed.



fly --target=us-east-2a login --concourse-url=http://ci.devops-ontap.com:8080 -n cisco-fso-labs --username=us-east-2a --password=us-east-2a!




fly -t ci set-pipeline -c pipeline-v2.yml -p us-east-2a -l /Users/sconrod/API-Trainings/dev/params/us-east-2a.yml -v aws.region=us-east-2 -v az.name=us-east-2a -v vault.addr=http://vault.devops-ontap.com:8200

