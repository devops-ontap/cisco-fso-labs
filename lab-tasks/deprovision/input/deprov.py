#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
import requests

#Import Lab Vars
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

#Inject the vault var vals into the ephemeral oci build container

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN') #This gets the vault token from the ephemeral build container

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "key_name"

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"key_name": name }

resp = requests.post(url, headers=headers, json=data_json)

print(resp.status_code)
