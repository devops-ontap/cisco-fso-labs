#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
import requests

url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"
payload='grant_type=client_credentials&client_id=fsolab4%40cisco-apipartnertraininglab&client_secret=cdb74fe0-a19e-4432-9350-9bb6ebc1fa56'
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)