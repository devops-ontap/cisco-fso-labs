#!/usr/bin/env python
#This Script creates the CSR from AMI and the key - split out the key
import json, re, sys, os, json, subprocess, time, sys
from subprocess import call, check_output

outfile_vars="vars"
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

keypair_name=name
sg_name=name
ami_id=csr_ami_id

path = os.getcwd()
print(path)
os.listdir(path)

#Tag the Instance with the name csr1000v
#aws ec2 create-key-pair --key-name MyKeyPair moved to aws prep

instance_type='t2.medium'
outfile_deploy_csr='deploy-csr.json'
outfile_get_vpcid='outfile_get_vpcid.json'

get_vpcid='aws ec2 describe-vpcs --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=' + "{}".format(name)
output = check_output("{}".format(get_vpcid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_vpcid, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_vpcid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Vpcs']
    question_data=question_access[0]
    replies_access=question_data['VpcId']
    vpcid=replies_access
    print(vpcid)
    vpcid_var=('vpcid=' + "'" + "{}".format(vpcid) + "'")

with open(outfile_vars, 'w') as my_file:
    my_file.write(vpcid_var + "\n")



#get the router security group id
#aws ec2 describe-security-groups --filters "Name=vpc-id,Values=vpc-01bdad153448ce387" --filters "Name=group-name,Values=sg01
#get_sgid='aws ec2 describe-security-groups --region' + " " + "{}".format(region) + " " + '--filters "Name=group-name,Values=' + "{}".format(sg_name) + '"' + " " + '"Name=availability-zone,Values=' + "{}".format(az) + '"'
outfile_get_sgid='outfile_sgid.json'
get_sgid='aws ec2 describe-security-groups --region' + " " + "{}".format(region) + " " + '--filters "Name=group-name,Values=' + "{}".format(sg_name) + '"'
output = check_output("{}".format(get_sgid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_sgid, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_sgid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['SecurityGroups']
    question_replies=question_access[0]
    question_data=question_replies['GroupId']
    sgid=question_data
    print(sgid)
    sgid_var=('sgid=' + "'" + "{}".format(sgid) + "'")
with open(outfile_vars, 'a+') as my_file:
    my_file.write(sgid_var + "\n")



#Get the router subnetid
outfile_get_subnetid_router='subnet_id_router.json'
get_subnetid_router='aws ec2 describe-subnets --region' + " " + "{}".format(region) + " " '--filters' + " " + '"Name=availability-zone,Values=' + "{}".format(az)  + '"' + " " + '"Name=tag:Name,Values=SUBNET_01_ROUTER"'
output = check_output("{}".format(get_subnetid_router), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

with open(outfile_get_subnetid_router, 'w') as my_file:
    my_file.write(output)
with open(outfile_get_subnetid_router) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access = read_content['Subnets']
    print(question_access)
    replies_access = question_access[0]
    print(replies_access)
    replies_data=replies_access['SubnetId']
    subnetid_router=replies_data
    print(subnetid_router)
    subnetid_router_var=('subnetid_router=' + "'" + "{}".format(subnetid_router) + "'")

with open(outfile_vars, 'a') as my_file:
    my_file.write(subnetid_router_var + "\n")

#get the subnetid_lan
outfile_get_subnetid_lan='outfile_subnetid_lan.json'
get_subnetid_lan='aws ec2 describe-subnets --region' + " " + "{}".format(region) + " " '--filters' + " " + '"Name=availability-zone,Values=' + "{}".format(az) + '"' + " " + '"Name=tag:Name,Values=SUBNET_01_LAN' + '"'
output = check_output("{}".format(get_subnetid_lan), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_get_subnetid_lan, 'w') as my_file:
    my_file.write(output)
with open(outfile_get_subnetid_lan) as access_json:
    read_content = json.load(access_json)
    print(read_content)
    question_access = read_content['Subnets']
    print(question_access)
     
    replies_access = question_access[0]
    replies_data=replies_access['SubnetId']
    subnetid_lan=replies_data
    print(subnetid_lan)
    subnetid_lan_var=('subnetid_lan=' + "'" + "{}".format(subnetid_lan) + "'")

with open(outfile_vars, 'a') as my_file:
    my_file.write(subnetid_lan_var + "\n")

  
    

#aws ec2 run-instances --image-id ami-067c66abd840abc24 --instance-type t2.medium --subnet-id subnet-008617eb0c9782f55 --security-group-ids sg-0b0384b66d7d692f9 --PrivateIpAddress "10.10.10.100" --associate-public-ip-address --key-name blitz-user-1
cmd_deploy_csr1000v='aws ec2 run-instances --region' + " " + "{}".format(region) + " " + '--image-id' + " " + "{}".format(ami_id) + " " + '--instance-type' + " " + "{}".format(instance_type) + " " + '--subnet-id' + " " + "{}".format(subnetid_router) +  " " + '--security-group-ids' + " " + "{}".format(sgid) + " " + '--associate-public-ip-address' + " " + '--key-name' + " " + "{}".format(keypair_name) + " " + '--placement AvailabilityZone=' + "{}".format(az)
#cmd_deploy_csr1000v='aws ec2 run-instances --image-id' + " " + "{}".format(ami_id) + " " + '--instance-type' + " " + "{}".format(instance_type) + " " + '--subnet-id' + " " + "{}".format(subnetid_router) +  " " + '--security-group-ids' + " " + "{}".format(router_sg_id) + " " + '--associate-public-ip-address' + " " + '--key-name' + " " + "{}".format(keypair_name)
#print(cmd_deploy_csr1000v)

output = check_output("{}".format(cmd_deploy_csr1000v), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

with open(outfile_deploy_csr, 'w') as my_file:
    my_file.write(output)


with open (outfile_deploy_csr) as access_json:
    read_content = json.load(access_json)
    question_access_csr = read_content['Instances']
    replies_access_csr = question_access_csr[0]
    replies_data_csr=replies_access_csr['InstanceId']
    print(replies_data_csr)
    csr1000v_instance_id=replies_data_csr #add this to the vars file
    print(csr1000v_instance_id)
    csr1000v_instance_id_var=('csr1000v_instance_id=' + "'" + "{}".format(csr1000v_instance_id) + "'")
    csr100v_int_ip_addr=replies_access_csr['PrivateIpAddress']
    print(csr100v_int_ip_addr)

with open(outfile_vars, 'a+') as my_file:
    my_file.write(csr1000v_instance_id_var + "\n")


#Capture the instance_id and write to the var file or vault
csr1000v_instance_id_var=('csr1000v_instance_id=' + "'" + "{}".format(csr1000v_instance_id) + "'")
print(csr1000v_instance_id_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(csr1000v_instance_id_var + "\n")

#tag the csr1000v
#tag_csr1000v='aws ec2 create-tags --resources' + " " + "{}".format(csr1000v_instance_id) '--tags "'Key="[Name]",Value=csr1000v'"
csr_tag_inst='aws ec2 create-tags --region' + " " + "{}".format(region) + " " + '--resources' + " " +  "{}".format(csr1000v_instance_id) + " " + '--tags' + " " + "'" + 'Key="Name",Value=csr1000v' + "'"
output = check_output("{}".format(csr_tag_inst), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Capture the private IP Address and write to the var file or vault
csr100v_int_ip_addr_var=('csr100v_int_ip_addr=' + "'" + "{}".format(csr100v_int_ip_addr) + "'")
print(csr100v_int_ip_addr_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(csr100v_int_ip_addr_var + "\n")


#Pole until the instance is created....
##!!HERE WE NEED TO POLL AND WAIT UNTIL THE INSTANCE IS IN AN INITIALIZED STATE -
#aws ec2 wait instance-status-ok --instance-ids csr1000v_instance_id
cmd_check_instance='aws ec2 wait instance-running --instance-ids' + " " + csr1000v_instance_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#Get the external public address assigned to the csr1000v and write it to the var file or vault
outfile_csr_pub_ip='csr_pub_ip.json'
cmd_get_csr_pub_ip='aws ec2 describe-instances --region' + " " + "{}".format(region) + " " '--instance-id' + " " + "{}".format(csr1000v_instance_id) + " " + '--query "Reservations[*].Instances[*].PublicIpAddress"'
output = check_output("{}".format(cmd_get_csr_pub_ip), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_csr_pub_ip, 'w') as my_file:
    my_file.write(output)

outfile_csr_pub_ip='csr_pub_ip.json'
with open(outfile_csr_pub_ip) as access_json:
    read_content = json.load(access_json)
    question_access = read_content[0]
    print(read_content)
    question_data=question_access[0]
    csr_pub_ip=question_data
    print(csr_pub_ip)


#Capture the External IP address and write it to the var file or vault
    csr_pub_ip_var=('csr_pub_ip=' + "'" + "{}".format(csr_pub_ip) + "'")
    print(csr_pub_ip_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(csr_pub_ip_var + "\n")

#Create a Secondary NIC and assign to the Lan subnet
#cmd_add_nic_router='aws ec2 create-network-interface --subnet-id' + " " + "{}".format(subnetid_lan) + " " + '--description "csr_nic"' + " " + '--groups' + " " + "{}".format(router_sg_id) + " " + '--private-ip-address 10.10.20.100'
outfile_add_csr_nic='add-csr-nic.json'
cmd_add_csr_nic='aws ec2 create-network-interface --region' + " " "{}".format(region) + " " + '--subnet-id' + " " + "{}".format(subnetid_lan) + " " + '--description "csr_nic_lan_sub"' + " " + '--groups' + " " + "{}".format(sgid) + " " + '--private-ip-address 10.10.20.101' + " " + '--tag-specifications' + " " + "'ResourceType=network-interface,Tags=[{Key=Name,Value=" + "{}".format(name) + '}]'"" + "'"
output = check_output("{}".format(cmd_add_csr_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_add_csr_nic, 'w') as my_file:
    my_file.write(output)

#Capture the secondar eni_id out of the json output
outfile_add_csr_nic='add-csr-nic.json'
with open(outfile_add_csr_nic) as access_json:
    read_content = json.load(access_json)
    question_access=read_content['NetworkInterface']
    question_data=question_access['NetworkInterfaceId']
    eni_id=question_data
#write the interface eni out to the vars file will  need it to attach it
    eni_id_var=('eni_id=' + "'" + "{}".format(eni_id) + "'")
    print(eni_id_var)
with open(outfile_vars, 'a') as my_file:
    my_file.write(eni_id_var + "\n")



#Associate the new NIC with the CSRV Instance ID
#aws ec2 attach-network-interface --network-interface-id eni-0dc56a8d4640ad10a --instance-id i-1234567890abcdef0 --device-index 1


outfile_attach_csr_nic='attach-csr-nic.json'
cmd_attach_csr_nic='aws ec2 attach-network-interface --region' + " " + "{}".format(region) + " " +  '--network-interface-id' + " " + "{}".format(eni_id) + " " + '--instance-id' + " " + "{}".format(csr1000v_instance_id) + " " + '--device-index 2'
output = check_output("{}".format(cmd_attach_csr_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_attach_csr_nic, 'w') as my_file:
    my_file.write(output)

#Wait to check the instance is initialized
#Check that the instance is initialized
cmd_check_instance='aws ec2 wait instance-status-ok --instance-ids' + " " + csr1000v_instance_id + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(cmd_check_instance), shell=True).decode().strip()
print("Output: \n{}\n".format(output))