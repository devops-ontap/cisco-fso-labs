#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
import requests

#The AppD secret is passed in via Env Var which is injected into the build container via the pipeline
#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
appd_secret = os.getenv('APPD_SECRET')
#APPD_SECRET='cdb74fe0-a19e-4432-9350-9bb6ebc1fa56'

url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"
payload='grant_type=client_credentials&client_id=fsolab4%40cisco-apipartnertraininglab&client_secret=' + str(appd_secret)
print(payload)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

#put the bearer token into a var
token_json = response.json()
appd_token = token_json['access_token']
print(appd_token)

os.environ["APPD_TOKEN"] = appd_token

#write the access token to the vault (remember need to update this later so it does it for each environment - so each branch needs to have a user in vault with that name
#Do this from the shell script until you add in the vault module for python here.....

