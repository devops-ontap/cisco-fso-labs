#!/usr/bin/env python
import json, re, sys, os, json
import subprocess
from subprocess import call, check_output

#MAKE SURE THE AWS IS UP TO VERSION 2 ON THE BUILD CONTAINER
#GET THE DEFAULT VPC ID
outfile_vars="vars"

lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

outfile_vars="vars"
sg_name=name

#1 - Create a Key Pair
keypair_name=name
outfile_key_pair = 'keypair_name' + '.json'

#CREATE THE NEW VPC01 AND GET VPCID
outfile = 'aws-vpc.json'
#cmd_deploy='aws ec2 create-vpc --region' + " " + "{}".format(region) + " " + '--cidr-block 10.10.0.0/16 --tag-specifications' + " " + "'ResourceType=vpc,Tags=[{Key=Name,Value=trainee1}]'"
cmd_deploy='aws ec2 create-vpc --region' + " " + "{}".format(region) + " " + '--cidr-block 10.10.0.0/16 --tag-specifications' + " " + "'ResourceType=vpc,Tags=[{Key=Name,Value=" + "{}".format(name) + '}]'"" + "'"
output = check_output("{}".format(cmd_deploy), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile, 'w') as my_file:
    my_file.write(output)
with open(outfile) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Vpc']
    replies_access = question_access['VpcId']
    vpcid = replies_access
    print(vpcid)
    vpcid_var=('vpcid=' + "'" + "{}".format(vpcid) + "'")
    print(vpcid_var)

with open(outfile_vars, 'a+') as my_file:
    my_file.write(vpcid_var + "\n")

#logon to the vault
token = os.getenv(SSH-TOKEN)
vault_login='vault login --no-print' + " " + SSH_TOKEN

#write the vpcid to the vault
put_vault_vpcid='vault kv put concourse/cisco-fso-labs/' + "{}".format(name) + vpcid_var
print(put_vault_vpcid)
output = check_output("{}".format(put_vault_vpcid, shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Create the keypair
create_keypair='aws ec2 create-key-pair --key-name' + " " +  "{}".format(name) + " " + '--region' + " " + "{}".format(region) + " " + '--availability-zone' + " " + "{}".format(az)


#CREATE THE ROUTER SUBNET
outfile_subnet_router = 'aws-subnet-router.json'
cmd_subnet_router='aws ec2 create-subnet --vpc-id' + " " + "{}".format(vpcid) + " " + '--region' + " " + "{}".format(region) + " " + '--availability-zone' + " " + "{}".format(az) + " " + '--cidr-block 10.10.10.0/24 --tag-specifications' + " " "'ResourceType=subnet,Tags=[{Key=Name,Value=SUBNET_01_ROUTER}]'"
print(cmd_subnet_router)
output = check_output("{}".format(cmd_subnet_router), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_subnet_router, 'w') as my_file:
    my_file.write(output)
with open (outfile_subnet_router) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Subnet']
    replies_access = question_access['SubnetId']
    subnetid_router = replies_access
    print(subnetid_router)
    subnetid_router_var=('subnetid_router=' + "'" + "{}".format(subnetid_router) + "'")

with open(outfile_vars, 'a+') as my_file:
    my_file.write(subnetid_router_var + "\n")

#CREATE THE LAN SUBNET
outfile_subnet_lan = 'aws-subnet-lan.json'
cmd_subnet_lan='aws ec2 create-subnet --vpc-id' + " " + "{}".format(vpcid) + " " + '--region' + " " + "{}".format(region) + " " + '--availability-zone' + " " + "{}".format(az) + " " + '--cidr-block 10.10.20.0/24 --tag-specifications' + " " "'ResourceType=subnet,Tags=[{Key=Name,Value=SUBNET_01_LAN}]'"
print(cmd_subnet_lan)
output = check_output("{}".format(cmd_subnet_lan), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_subnet_lan, 'w') as my_file:
    my_file.write(output)
with open (outfile_subnet_lan) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Subnet']
    replies_access = question_access['SubnetId']
subnetid_lan = replies_access
print(subnetid_lan)

subnetid_lan_var=('subnetid_lan=' + "'" + "{}".format(subnetid_lan) + "'")

with open(outfile_vars, 'a+') as my_file:
    my_file.write(subnetid_lan_var + "\n")


#CREATE INTERNET GATEWAY
outfile_ig = 'aws-ig.json'
cmd_ig='aws ec2 create-internet-gateway --region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=internet-gateway,Tags=[{Key=Name,Value=IG}]'"
print(cmd_ig)
output = check_output("{}".format(cmd_ig), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_ig, 'w') as my_file:
    my_file.write(output)
with open (outfile_ig) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access = read_content['InternetGateway']
    print(question_access)
    replies_access = question_access['InternetGatewayId']
    print(replies_access)
igid = replies_access
print(igid)

igid_var=('igd=' + "'" + "{}".format(igid) + "'")

with open(outfile_vars, 'a+') as my_file:
    my_file.write(igid_var + "\n")

#Attach Internet Gateway to the VPC
outfile_ig_attach_log = 'ig_attach_log.json'
cmd_ig_attach='aws ec2 attach-internet-gateway' + " " + '--region' + " " + "{}".format(region) + " " + '--internet-gateway-id' + " " + "{}".format(igid) + " " + '--vpc-id' + " " + "{}".format(vpcid)
print(cmd_ig_attach)
output = check_output("{}".format(cmd_ig_attach), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
#Do we need to add any var here to the vars.py??


#Get the route table id for the default route table for the new vpc
outfile_get_vpc_rt_id='get-vpc-rt-id.json'
get_vpc_rt_id='aws ec2 describe-route-tables' + " " + '--region' + " " + "{}".format(region) + " " + '--filters \"Name=vpc' + '-' + 'id,Values=' + "{}".format(vpcid) + '"' + " " + '--query "RouteTables[]"'
output = check_output("{}".format(get_vpc_rt_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_vpc_rt_id , 'w') as my_file:
    my_file.write(output)
with open (outfile_get_vpc_rt_id ) as access_json:
    read_content=json.load(access_json)
    question_access=read_content[0]
    replies_access=question_access['Associations']
    replies_data=replies_access[0]
    def_vpc_rt_id=replies_data['RouteTableId']
    print(def_vpc_rt_id)


def_vpc_rt_id_var=('def_vpc_rt_id=' + "'" + "{}".format(def_vpc_rt_id) + "'")
with open(outfile_vars, 'a+') as my_file:
    my_file.write(def_vpc_rt_id_var + "\n")

#Tag the default rout table --resources   --tags Key=Name,Value=DEFAULT_RT

#aws ec2 create-tags
tag_def_vpc_rt='aws ec2 create-tags --resources --region' + " " + "{}".format(region) + " " + " " + "{}".format(def_vpc_rt_id) + " " + '--tags Key=Name,Value=DEFAULT_RT_' + "{}".format(name)
output = check_output("{}".format(tag_def_vpc_rt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#Add a new route to the default vpc route table requires the default vpc route table id and assoicatiate and the default gatewayid
outfile_ass_rt = 'ass_rt.json'
ass_rt_default_rt='aws ec2 create-route' + " " + '--region' + " " + "{}".format(region) + " " + '--route-table-id' + " " + "{}".format(def_vpc_rt_id) + " " + '--destination-cidr-block 0.0.0.0/0 --gateway-id' + " " + igid
output = check_output("{}".format(ass_rt_default_rt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_ass_rt, 'w') as my_file:
    my_file.write(output)

#Create LAN Route Table
outfile_rt_lan = 'aws-rt-lan.json'
cmd_rt_lan='aws ec2 create-route-table --vpc-id' + " " + "{}".format(vpcid) + " " + '--region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=route-table,Tags=[{Key=Name,Value=LAN_RT}]'"
print(cmd_rt_lan)
output = check_output("{}".format(cmd_rt_lan), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_rt_lan, 'w') as my_file:
    my_file.write(output)
with open (outfile_rt_lan) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['RouteTable']
    replies_access = question_access['RouteTableId']
rt_lan_id = replies_access
print(rt_lan_id)

rt_lan_id_var=('rt_lan_id=' + "'" + "{}".format(rt_lan_id) + "'")
with open(outfile_vars, 'a+') as my_file:
    my_file.write(rt_lan_id_var + "\n")

#Create ROUTER Route Table
outfile_rt_rt = 'aws-rt-router.json'
cmd_rt_rt='aws ec2 create-route-table --vpc-id' + " " + "{}".format(vpcid) + " " + '--region' + " " + "{}".format(region) + " " + '--tag-specifications' + " " + "'ResourceType=route-table,Tags=[{Key=Name,Value=ROUTER_RT}]'"
print(cmd_rt_rt)
output = check_output("{}".format(cmd_rt_rt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_rt_rt, 'w') as my_file:
    my_file.write(output)
with open (outfile_rt_rt) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['RouteTable']
    replies_access = question_access['RouteTableId']
rt_rt_id = replies_access
print(rt_rt_id)

rt_rt_id_var=('rt_rt_id=' + "'" + "{}".format(rt_rt_id) + "'")
with open(outfile_vars, 'a+') as my_file:
    my_file.write(rt_rt_id_var + "\n")

#ASSOCIATE THE LAN ROUTE TABLE WITH THE LAN SUBNET
outfile_ass_lan_sub = 'ass_rt_lan_sub.json'
ass_rt_lan_sub='aws ec2 associate-route-table --region' + " " + "{}".format(region) + " " + '--route-table-id' + " " + "{}".format(rt_lan_id) + " " + '--subnet-id' + " " + "{}".format(subnetid_lan)
print(ass_rt_lan_sub)
output = check_output("{}".format(ass_rt_lan_sub), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_ass_lan_sub, 'w') as my_file:
    my_file.write(output)

'''
#ASSOCIATE THE ROUTE ROUTE TABLE WITH THE ROUTER LAN
outfile_ass_rt_sub = 'ass_rt_router_sub.json'
ass_rt_sub='aws ec2 associate-route-table' + " " + '--region' + " " + "{}".format(region) + " " + '--route-table-id' + " " + "{}".format(rt_rt_id) + " " +  '--subnet-id' + " " + "{}".format(subnetid_router)
print(ass_rt_sub)
output = check_output("{}".format(ass_rt_sub), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_ass_rt_sub, 'w') as my_file:
    my_file.write(output)
'''
#3 - Create a Security Group
out_file_sg_router='outfile-sg-router.json'
cmd_security_group='aws ec2 create-security-group --group-name --region' + " " + "{}".format(region) + " " + " " + "{}".format(sg_name) + " " + '--description' + " " + "{}".format(sg_name) + " " + '--vpc-id' + " " + "{}".format(vpcid)
output = check_output("{}".format(cmd_security_group), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(out_file_sg_router, 'w') as my_file:
    my_file.write(output)
with open (out_file_sg_router) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['GroupId']
    router_sg_id=question_access
    router_sg_id_var=('router_sg_id=' + "'" + "{}".format(router_sg_id) + "'")
    print(router_sg_id_var)
with open(outfile_vars, 'a+') as my_file:
    my_file.write(router_sg_id_var + "\n")

#Create inbound rule on the security group to allow SSH
#aws ec2 authorize-security-group-ingress --group-id sg-1234567890abcdef0 --protocol tcp --port 22 --cidr 0.0.0.0/0
auth_inbound_ssh='aws ec2 authorize-security-group-ingress --region' + " " + "{}".format(region) + " " + '--group-id' + " " "{}".format(router_sg_id) + " " + '--protocol tcp --port 22 --cidr 0.0.0.0/0'
output = check_output("{}".format(auth_inbound_ssh), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

