#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time
from subprocess import call, check_output

#UNDER DEV DO NOT USE YET!!!!!!!!

outfile_vars="vars"
lab_vars='lab_vars.py'
from lab_vars import *

get_vpcid='aws ec2 describe-vpcs --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=' + "{}".format(name)
output = check_output("{}".format(get_vpcid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
outfile_get_vpcid='vpcid.json'
with open(outfile_get_vpcid, 'w') as my_file:
    my_file.write(output)
with open (outfile_get_vpcid) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Vpcs']
    question_data=question_access[0]
    replies_access=question_data['VpcId']
    vpcid=replies_access
    print(vpcid)



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
''''
for instanceid in data:
    output = check_output("{}".format('aws ec2 terminate-instances --instance-id '+(instanceid[0]) + " " + '--region' + " " "{}".format(region)), shell=True).decode().strip()
    print("Output: \n{}\n".format(output))

#Poll the instance state for each of the instanceIDs before proceeding...
#Pole until the instance is fully terminated....
#aws ec2 wait instance-status-ok --instance-ids csr1000v_instance_id
#aws ec2 wait instance-terminated --instance-ids i-1234567890abcdef0
for instanceid in data:
    output = check_output("{}".format('aws ec2 wait instance-terminated --instance-id '+(instanceid[0]) + " " + '--region' + " " "{}".format(region)), shell=True).decode().strip()
    print("Output: \n{}\n".format(output))
    
    
#Poll to determine when terminated status is set    

#Get the NIC ID
#aws ec2 describe-network-interfaces --region us-west-1 --filters "Name=description,Values=csr_nic_lan_sub" "Name=tag:Name,Values=us-west-1a" --query "NetworkInterfaces[*].NetworkInterfaceId" --output text
csr_nic_id='aws ec2 describe-network-interfaces --region' + " " "{}".format(region) + " " + '--filters Name=description,Values=csr_nic_lan_sub' + " " +  'Name=tag:Name,Values=' + "{}".format(az) + " " + '--query' + " " + '"NetworkInterfaces[*].NetworkInterfaceId"' + " " '--output text'
output = check_output("{}".format(csr_nic_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#DELETE NETWORK INTERFACES
delete_nic='delete-network-interface --network-interface-id' + " " + "{}".format(csr_nic_id)
output = check_output("{}".format(delete_nic), shell=True).decode().strip()
print("Output: \n{}\n".format(output))


#get the security group id
get_sgid='aws ec2 describe-security-groups --region' + " " + "{}".format(region) + " " '--filters Name=group-name' + ',Values=' + "{}".format(name) + " " + 'Name=vpc-id,Values=' + "{}".format(vpcid) + " " + '--query' + " " + '"SecurityGroups[*].GroupId"' + " " '--output text'
output = check_output("{}".format(get_sgid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#delete the security group id
outfile_sgid='sgid.json'
with open(outfile_sgid, 'w') as my_file:
    my_file.write(output + "\n")

print(output)
output = check_output("{}".format('aws ec2 delete-security-group --group-id '+ " " + "{}".format(output) + " " + '--region' + " " "{}".format(region)), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
'''

#Delete the key

#Delete the route tables
#GET THE ROUTE TABLES
get_rt='aws ec2 describe-route-tables --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=ROUTER_RT' + " " + '--query' + " " + '"RouteTables[*].RouteTableId"' + " " '--output text'
output = check_output("{}".format(get_rt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
rt_rt_id=output
print(rt_rt_id)

#NEED TO GET THE ROUTE TABLE ASSOCIATION AND REMOVE IT BEFORE YOU CAN DELETE THE ROUTE TABLE


print('Printing.....')
del_rt_rt_id='aws ec2 delete-route-table --route-table-id' + " " + "{}".format(rt_rt_id)
output = check_output("{}".format(del_rt_rt_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

get_rt='aws ec2 describe-route-tables --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=LAN_RT' + " " + '--query' + " " + '"RouteTables[*].RouteTableId"' + " " '--output text'
output = check_output("{}".format(get_rt), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
rt_lan_id=output
print(rt_lan_id)

del_rt_lan_id='aws ec2 delete-route-table --route-table-id' + " " + "{}".format(rt_lan_id) + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(del_rt_lan_id), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#DELETE THE ROUTE TABLES


#Delete the subnets
#GET THE SUBNETS
get_subnets='aws ec2 describe-subnets --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=SUBNET_01_ROUTER' + " " + '--query' + " " + '"Subnets[*].SubnetId"' + " " '--output text'
output = check_output("{}".format(get_subnets), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
subnet_rt_id=output
print(subnet_rt_id)

get_subnets='aws ec2 describe-subnets --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=SUBNET_01_LAN' + " " + '--query' + " " + '"Subnets[*].SubnetId"' + " " '--output text'
output = check_output("{}".format(get_subnets), shell=True).decode().strip()
print("Output: \n{}\n".format(output))
subnet_lan_id=output
print(subnet_lan_id)

#DELETE THE SUBNETS

'''
#Delete the Internet Gateway
get_ig='aws ec2 describe-internet-gateways --region' + " " + "{}".format(region) + " " + '--filters Name=tag:Name,Values=IG' + " " + '--query' + " " + '"InternetGateways[*].InternetGatewayId"' + " " '--output text'
output = check_output("{}".format(get_ig), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

igid=output

del_igid='aws ec2 delete-internet-gateway' + " " + '--internet-gateway-id' + " " + "{}".format(igid) + '--filters Name=tag:Name,Values=IG' + " " + '--region' + "{}".format(region)
output = check_output("{}".format(del_igid), shell=True).decode().strip()
print("Output: \n{}\n".format(output))






#DELETE VPC
delete_vpc='aws ec2 delete-vpc --vpc-id' + " " + "{}".format(vpcid) + " " + '--region' + " " + "{}".format(region)
output = check_output("{}".format(delete_vpc), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

'''

