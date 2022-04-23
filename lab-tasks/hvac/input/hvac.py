#!/usr/bin/env python
import json, re, sys, os, json, subprocess, requests
from subprocess import call, check_output

lab_vars='lab_vars.py'
from lab_vars import *

#write the vpcid to the vault

put_vault_vpcid='vault kv put concourse/cisco-fso-labs/' + "{}".format(name) +
output = check_output("{}".format(put_vault_vpcid, shell=True).decode().strip()
print("Output: \n{}\n".format(output))

APPD_OATH_TOKEN=output
print(APPD_OATH_TOKEN)

url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/zero/v1beta/install/agentVersions?latest=true"

payload={}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer + APPD_OATH_TOKEN
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)





