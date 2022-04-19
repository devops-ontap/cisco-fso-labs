#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()


url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"

payload='grant_type=client_credentials&client_id=sconrod%40cisco-apipartnertraininglab&client_secret=3c4d7f17-536f-4e0c-8dfd-403bc2cf2c6d'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
