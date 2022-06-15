#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
token = os.getenv('TE_OATHTOKEN')
url = "https://api.thousandeyes.com/v6/status.json"
payload={}
headers = {'Authorization': 'Bearer ' + token}
response = requests.request("GET", url, headers=headers, data=payload)

json = response.json()
print(json)


