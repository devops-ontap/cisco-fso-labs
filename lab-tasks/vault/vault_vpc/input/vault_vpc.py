#!/usr/bin/env python
import json, re, sys, os, json, hvac
import subprocess
from subprocess import call, check_output
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *
import hvac

os.environ['VAULT_TOKEN'] = 'VAULT_ADDR'
os.environ['VAULT_ADDR'] = 'VAULT_TOKEN'

import requests
from requests.structures import CaseInsensitiveDict

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/us-east-2a/vpcid"

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = "s.s1UuURYXGclHOSQz5MhTrdWS"

resp = requests.get(url, headers=headers)
print(resp.text)
print(type(resp.text))

json_object = json.loads(resp.text)
print(type(json_object))

print(json_object)
print(json_object["data"])

print(json_object["data"])







