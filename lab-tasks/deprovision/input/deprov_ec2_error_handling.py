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


name='us-west-1a'
#Get List of all EC2 instances in a AZ
#aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='us-east-2c']|[0].Value}" --output json
#aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key=='us-east-2c']|[0].Value}" --output json --filters Name=instance-state-name, Values=running
cmd_describe_instances='aws ec2 describe-instances --query "Reservations[*].Instances[*].{Instance:InstanceId,AZ:Placement.AvailabilityZone,Name:Tags[?Key==' + "'" "{}".format(name) + "'" + ']|[0].Value}"' + " " + '--output json' + " " + '--filters Name=instance-state-name,Values=running'
output = check_output("{}".format(cmd_describe_instances), shell=True).decode().strip()
y=json.loads(output)
list_json = y
list_of_lists=list_json
flatList = [ item for elem in list_of_lists for item in elem]
res = [ sub['Instance'] for sub in flatList ]
#print(str(res))

if len(res) == 0:
    sys.exit("No Running Instances....Exiting.....")


#Check if the array is null and if so exit script.

res_json = json.dumps(res)
print(res_json)
#Must write res to file
file = 'instances.json'

with open(file, 'w', encoding='utf-8') as f:
    json.dump(res_json, f)

#For each instance Id in the list res, delete it
#aws ec2 terminate-instances --instance-ids

#aws ec2 terminate-instances --instance-ids '["i-02ee4d941d2fd488e", "i-02fab0ce23bb8ee99", "i-04f6e2a5ea79aa903", "i-059eda602079d5c74", "i-039c7783f6e2f577a"]'
cmd_terminate_instances='aws ec2 terminate-instances --instance-ids' + " " + "'" + res_json + "'"
output = check_output("{}".format(cmd_terminate_instances), shell=True).decode().strip()

#Poll to for terminated status
cmd_check_instance='aws ec2 wait instance-terminated --instance-ids' + " " + "'" + res_json + "'" + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

