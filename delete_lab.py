#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time
from subprocess import call, check_output

outfile_vars="vars"
lab_vars='lab_vars.py'
from lab_vars import *
''''
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
'''

#Get All Instances in the AZ for the Region and VPC write a for each loop here
#aws ec2 describe-instances --region us-west-1 --filters Name=availability-zone,Values=us-west-1a --query "Reservations[*].Instances[*].InstanceId" --output text
outfile_instanceids='inst_ids.json'
get_instances='aws ec2 describe-instances --region' + " " + "{}".format(region) + " " + '--filters Name=availability-zone,Values=' + "{}".format(az) + " " + '--query' + " " + '"Reservations[*].Instances[*].InstanceId"' + " " + '--output json'
output = check_output("{}".format(get_instances), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
with open(outfile_instanceids, 'w') as my_file:
    my_file.write(output + "\n")

print(type(output))

with open(outfile_instanceids) as data_file:
    data = json.load(data_file)
    for instanceid in data:
        print(instanceid[0])

for instanceid in data:
    output = check_output("{}".format('aws ec2 terminate-instances --instance-id '+(instanceid[0]) + " " + '--region' + " " "{}".format(region)), shell=True).decode().strip()
    print("Output: \n{}\n".format(output))






#Get the NIC ID
#aws ec2 describe-network-interfaces --region us-west-1 --filters "Name=description,Values=csr_nic_lan_sub" "Name=tag:Name,Values=us-west-1a" --query "NetworkInterfaces[*].NetworkInterfaceId" --output text
csr_nic_id='aws ec2 describe-network-interfaces --region' + " " "{}".format(region) + " " + '--filters Name=description,Values=csr_nic_lan_sub' + " " +  'Name=tag:Name,Values=' + "{}".format(az) + " " + '--query' + " " + '"NetworkInterfaces[*].NetworkInterfaceId"' + " " '--output text'
output = check_output("{}".format(csr_nic_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#DELETE NETWORK INTERFACES
delete_nic='delete-network-interface --network-interface-id' + " " + "{}".format(csr_nic_id)
output = check_output("{}".format(delete_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))



#DELETE VPC
delete_vpc='aws ec2 delete-vpc' + " " + "{}".format(vpcid)
output = check_output("{}".format(delete_vpc), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
'''
