#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()

#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
APPD_SECRET = os.getenv('APPD_SECRET')
#APPD_SECRET='cdb74fe0-a19e-4432-9350-9bb6ebc1fa56'

url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"
payload='grant_type=client_credentials&client_id=fsolab4%40cisco-apipartnertraininglab&client_secret=' + str(APPD_SECRET)
print(payload)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
print(response.json)

#write the access token to the vault


#put the bearer token into a var
token_json = response.json()
appd_token = token_json['access_token']
print(appd_token)

#save it to a json file and add that json file to the vault...
outfile='token.json'
with open(outfile, 'w') as my_file:
    my_file.write(appd_token)


