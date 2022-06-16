Getting Started
==================

Before you can do work to the App Dynamics API, you must perform some manual steps in the GUI:

Logon to the lab account as an Account Owner
Select the Gear Icon in the top right corner
Select Administration
Select the API Client TAb
select the account or add a new account, and ensure it has the "Account Owner" role
select generate secret, copy the secret and enter it into the vault OR if you are just running an initial test paste the secret into your code.
select the save button on the far right 



This script will return a temporary OATH BEARER Token that you can then write to the vault.

The secret is set forever until you change it manually via the GUI or via the API
As a best practise, just change it with each API call. 






https://docs.appdynamics.com/21.6/en/extend-appdynamics/appdynamics-apis/api-clients

Installing appdynamics python module
https://docs.appdynamics.com/22.4/en/application-monitoring/install-app-server-agents/python-agent/python-agent-api/python-agent-api-reference


