#!/usr/bin/env python
import json, re, sys, os, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
APPD_OATH_TOKEN = os.getenv('APPD_OATH_TOKEN')
STR_APPD_OATH_TOKEN=str(APPD_OATH_TOKEN)

#url="https://cisco-apipartnertraininglab.saas.appdynamics.com/zero/v1beta/install/agentVersions?latest=true"
#url="https://cisco-apipartnertraininglab.saas.appdynamics.com/controller/rest/applications?output=JSON"
#url="https://cisco-apipartnertraininglab.saas.appdynamics.com/controller/rest/applications/Supercar-Trader/business-transactions"
#url="https://cisco-apipartnertraininglab.saas.appdynamics.com/controller/rest/applications/Supercar-Trader/metrics"
#url="https://cisco-apipartnertraininglab.saas.appdynamics.com/controller/rest/applications?output=JSON"

url="https://cisco-apipartnertraininglab.saas.appdynamics.com/controller/rest/applications/Supercar-Trader/business-transactions?output=JSON"

payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + STR_APPD_OATH_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
print(response.json)







