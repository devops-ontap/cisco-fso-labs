#!/usr/bin/env python
import json, re, sys, os, json, requests, urllib3
import subprocess
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')
token=str(VAULT_TOKEN)


url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/us-east-2a/vpcid"

headers = CaseInsensitiveDict()
headers = {"X-Vault-Token":VAULT_TOKEN}


resp = requests.get(url, headers=headers)
print(resp.text)
print(type(resp.text))

json_object = json.loads(resp.text)
print(type(json_object))

key_value= json_object['data']
print(key_value)

if "vpcid" in key_value:
    print(key_value["vpcid"])





