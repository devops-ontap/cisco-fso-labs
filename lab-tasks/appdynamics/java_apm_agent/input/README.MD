Instructor
===========

A Centos Instance with Tomcat and the JAVA App Super Car Trader installed with the AppD JAVA Agent.
When you are ready to cover modules for this part of the lab, run the task to turn on the Centos Instance.
Logon to the AppD Console to see the Agent Register.

After this we will Deploy the Same App as a Kubernetes Deployment with the JAVA Agent and look at both via the Console
Then we will proceed to interact via the AppD API with these objects.

The controller-info.xml exists in the vault in base64 encoding since it contains the root SAAS environment account number and secret
To retrieve programmatically via vault in the code:

$vault kv get -field data concourse/cisco-fso-labs/appd-helm-values | base64 -d > values.yaml

Note: When pulling helm chart values in base 64 from vault - these must first exist in git. So the flow should be:
new version of the values.yml in git without the account specifics hard coded (paramaterized)
Then have vault pass in those params to that file.

Right now I am just keeping entire values.yml file in the vault.

