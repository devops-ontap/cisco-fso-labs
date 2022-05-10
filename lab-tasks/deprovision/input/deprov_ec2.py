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

#Get List of all EC2 instances in a AZ
#aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='us-east-2c']|[0].Value}" --output json
#aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='us-east-2a']|[0].Value}" --output json
outfile='ec2_instances.json'
cmd_describe_instances='aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==' + "'" "{}".format(name) + "'" + ']|[0].Value}"' + " " + '--output json'
output = check_output("{}".format(cmd_describe_instances), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile, 'w') as my_file:
    my_file.write(output)
with open(outfile) as access_json:
    list_json = json.load(access_json)
    list_of_lists=list_json
    print(list_of_lists)
    print(type(list_of_lists))

flatList = [ item for elem in list_of_lists for item in elem]
print(flatList)

res = [ sub['Instance'] for sub in flatList ]
print(str(res))