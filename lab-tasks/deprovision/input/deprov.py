#!/usr/bin/env python
import json, re, sys, os, json, time, logging, requests, urllib3
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
from requests.structures import CaseInsensitiveDict
import subprocess
from subprocess import call, check_output

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN') #This gets the vault token from the ephemeral build container

lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

#get all the vars and then import this module to a delete_env script that uses the aws-cli commands and polls for inst state when termed

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "key_name"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
#data = f'{{"token": "{TOKEN}"}}'
data_json = {"key_name": name }
resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)

#Read vpcid  from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + vpcid

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"vpcid": vpcid }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)


#3 Read the subnetid_router from vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + subnetid_router

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"subnetid_router": subnetid_router }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)

#4 Read the subnetid_lan from vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + subnetid_lan

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"subnetid_lan": subnetid_lan }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)

#5 Read the igid from vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + igid

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"igid": igid }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)

#10 - Read rt_lan_id from vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + rt_lan_id

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"rt_lan_id": rt_lan_id }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)

#11 - Read rt_rt_id from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + rt_rt_id

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"rt_rt_id": rt_rt_id }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)

#13 - Read the router_sg_id from vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + router_sg_id

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"router_sg_id": router_sg_id }

resp = requests.get(url, headers=headers, json=data_json)
print(resp.status_code)