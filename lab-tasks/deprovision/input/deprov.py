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
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "ssh-key"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
key_name_json = resp.json()
print(key_name_json)
key_name_dict = key_name_json['Key']
key_name = key_name_dict['ssh-key']



#Read vpcid  from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "vpcid"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
vpcid_json = resp.json()
vpcid_dict = vpcid_json['data']
vpcid = vpcid_dict['vpcid']
print(vpcid)


#3 Read the subnetid_router from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "subnetid_router"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
subnetid_router = resp.json()
subnetid_router_dict = subnetid_router['data']
subnetid_router_id = subnetid_router_dict['subnetid_router']
print(subnetid_router_id)




#4 Read the subnetid_lan from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "subnetid_lan"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
subnetid_lan_json = resp.json()
subnetid_lan_dict = subnetid_lan_json['data']
subnetid_lan_id = subnetid_lan_dict['subnetid_lan']
print(subnetid_lan_id)



#5 Read the igid from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "igid"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
igid_json = resp.json()
igid_dict = igid_json['data']
igid = igid_dict['igid']
print(igid)

#aws ec2 delete-internet-gateway --internet-gateway-id $igid

#10 - Read rt_lan_id from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "rt_lan_id"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
rt_lan_id_json = resp.json()
rt_lan_id_dict = rt_lan_id_json['data']
rt_lan_id = rt_lan_id_dict['rt_lan_id']
print(rt_lan_id)

#aws ec2 delete-route-table --route-table-id $rt_lan_id

#11 - Read rt_rt_id from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "rt_rt_id"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
rt_rt_id_json = resp.json()
rt_rt_id_dict = rt_rt_id_json['data']
rt_rt_id = rt_lan_id_dict['rt_rt_id']
print(rt_rt_id)


#11 - Read rt_lan_id from vault
url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "rt_lan_id"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
rt_lan_id_json = resp.json()
rt_lan_id_dict = rt_lan_id_json['data']
rt_lan_id = rt_lan_id_dict['rt_lan_id']
print(rt_lan_id)



#13 - Read the router_sg_id from vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/" + name + "/" + "router_sg_id"
headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = VAULT_TOKEN
headers["Content-Type"] = "application/json"
data_json = {}
resp = requests.request("GET", url, headers=headers, json=data_json)
print(resp.json)
print(resp.status_code)
router_sg_id_json = resp.json()
router_sg_id_dict = router_sg_id_json['data']
router_sg_id = router_sg_id_dict['router_sg_id']
print(router_sg_id)


#AWS should be authenticated in the build container via the task args..


'''


#Delete the Route Tables

#aws ec2 delete-route-table --route-table-id rt_rt_id
cmd_del_rt_rt_id='aws ec2 delete-route-table --route-table-id' + " " + "{}".format(rt_rt_id)
print(cmd_del_rt_rt_id)
output = check_output("{}".format(cmd_del_rt_rt_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#aws ec2 delete-route-table --route-table-id rt_lan_id
cmd_del_rt_lan_id='aws ec2 delete-route-table --route-table-id' + "{}".format(rt_lan_id)
print(cmd_del_rt_lan_id)
output = check_output("{}".format(cmd_del_rt_lan_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#aws ec2 delete-internet-gateway --internet-gateway-id igid
cmd_del_igid='aws ec2 delete-internet-gateway --internet-gateway-id' + " "  + "{}".format(igid)
print(cmd_del_igid)
output = check_output("{}".format(cmd_del_igid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#Delete the subnets

#aws ec2 delete-subnet
cmd_del_router_sg_id='aws ec2 delete-subnet --subnet-id' + " " + "{}".format(subnetid_router)
print(cmd_subnetid_router)
output = check_output("{}".format(cmd_rsubnetid_router), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#aws ec2 delete-subnet
cmd_del_subnetid_lan='aws ec2 delete-subnet --subnet-id' " " + "{}".format(subnetid_lan)
print(cmd_subnetid_lan)
output = check_output("{}".format(cmd_subnetid_lan), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Delete the Internet Gateway
#aws ec2 delete-internet-gateway --internet-gateway-id igid
cmd_del_igid='aws ec2 delete-internet-gateway --internet-gateway-id' " " + "{}".format(igid)
output = check_output("{}".format(cmd_del_igid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Delete the Keys
#aws ec2 delete-key-pair --key-name
cmd_del_keys='aws ec2 delete-key-pair --key-name' + " " + "{}".format(key_name)
print(cmd_del_keys)
output = check_output("{}".format(cmd_del_keys), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Delete the VPC
cmd_del_vpc='aws ec2 delete-vpc --vpc-id' + " " + "{}".format(vpcid)
print(cmd_del_vpc)
output = check_output("{}".format(cmd_del_vpc), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


'''



