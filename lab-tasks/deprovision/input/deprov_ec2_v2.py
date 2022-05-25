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
#cmd_describe_instances='aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==' + "'" "{}".format(name) + "'" + ']|[0].Value}"' + " " + '--output json'
cmd_describe_instances='aws ec2 describe-instances --region us-east-2 --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==' + "'" "{}".format(name) + "'" + ']|[0].Value}"' + " " + '--filters Name=instance-state-code,Values=16 ' + " " + 'Name=availability-zone,Values=' + name + " " + '--output json'
#cmd_describe_instances='aws ec2 describe-instances --region' + " " + region + " " + '--filters Name=instance-state-code,Values=16 Name=availability-zone,Values=' + name
print(cmd_describe_instances)
output = check_output("{}".format(cmd_describe_instances), shell=True).decode().strip()
print(output)

y=json.loads(output)
print(y)
print(type(y))

#Here we have a list of lists that contain dictionaries - next flatten list
flatList = [ item for elem in y for item in elem]
res = [ sub['Instance'] for sub in flatList ]
print(res)
print(type(res))
file='instances.json'
with open(file, 'w') as my_file:
    my_file.write(output)

#For AWS CLI to accept this list of instances, it must be in format:
import pandas as pd
df = pd.read_json (r'instances.json')
df.to_csv (r'instances.txt', index = False)

#Terminate the Instances returned in the list...
cmd_term_instances='aws ec2 terminate-instances --filters instances.json
print(cmd_term_instances)
#output = check_output("{}".format(cmd_term_instances), shell=True).decode().strip()
#print("Output: \n{}\n".format(output))