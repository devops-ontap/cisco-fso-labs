#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
import requests

def get_appd_token():
    """
    This function will find get the appd ephemeral token by calling the secret from the vault,
    requesting the token, and writing the token to the vault
    """

#The AppD secret is passed in via Env Var which is injected into the build container via the pipeline
#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
secret = os.getenv('APPD_SECRET')


url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"
payload='grant_type=client_credentials&client_id=fsolab4%40cisco-apipartnertraininglab&client_secret=' + secret
print(payload)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)


token_json = response.json()
print(token_json)
TOKEN = token_json['access_token']

#write the token to a json file called data.json
outfile = 'token.json'
with open(outfile, 'w') as my_file:
    my_file.write(TOKEN)
my_file.close()


#write the appd oath token returned from the api call to the vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath"

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')

headers = CaseInsensitiveDict()
headers = {"X-Vault-Token":VAULT_TOKEN}
headers = {"Content-Type: application/json"}
data = '{"data":{"token":TOKEN}'
resp = requests.post(url=url,data=data)
print(resp.text)
print(type(resp.text))


#Here we are writing the temporary token for AppDynamics into the vault, so we may call it as a variable in subsequent API calls.
#we need to put this in a module form, so that each time we perform API calls we get a new token
import requests
from requests.structures import CaseInsensitiveDict

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath"

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"

#data = f'{{"token": "{TOKEN}"}}'
data_json = {"token": TOKEN}

resp = requests.post(url, headers=headers, json=data_json)

print(resp.status_code)
