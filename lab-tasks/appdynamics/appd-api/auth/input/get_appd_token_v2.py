#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
import requests

#The AppD secret is passed in via Env Var which is injected into the build container via the pipeline
#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
secret = os.getenv('APPD_SECRET')
#APPD_SECRET='cdb74fe0-a19e-4432-9350-9bb6ebc1fa56'

url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"
payload='grant_type=client_credentials&client_id=fsolab4%40cisco-apipartnertraininglab&client_secret=' + secret
print(payload)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)


token_json = response.json()
TOKEN = token_json['access_token']
print(TOKEN)

#write the appd oath token returned from the api call to the token the vaul

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath"

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')
token=str(VAULT_TOKEN)

headers = CaseInsensitiveDict()
headers = {"X-Vault-Token":VAULT_TOKEN}
headers = {"Content-Type: application/json"}
data = '{"data":{"token":"TOKEN"}}'
resp = requests.post(url=url,data=data)
print(resp.text)
print(type(resp.text))




