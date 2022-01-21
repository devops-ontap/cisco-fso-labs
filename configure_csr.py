#!/usr/bin/env python
import json, re, sys, os, json, subprocess
from subprocess import call, check_output
import netmiko
from netmiko import *

lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *
outfile_vars='vars.py'

#Get the csr10000v instance-id
#aws ec2 describe-instances --region us-east-2 --filters "Name=availability-zone,Value=us-east-2a" "Name=tag:name,Value=csr1000v
outfile_csr_inst='csr_id.json'
cmd_get_csr1000v_inst_id='aws ec2 describe-instances --region' + " " + "{}".format(region) + " " + '--filters' + " " + '"Name=availability-zone,Value=' + "{}".format(az) + '"'
output = check_output("{}".format(cmd_get_csr_pub_ip), shell=True).decode().strip()
print("Output: \n{}\n".format(output)

'''
#Get the instance ID and write it to the vars file
with open (outfile_csr_inst) as access_json:
    read_content = json.load(access_json)
    question_access = read_content['Instances']
    replies_access = question_access[0]
    replies_data=replies_access['InstanceId']
    print(replies_data)
    csr1000v_instance_id=replies_data
'''

#Get the external public address assigned to the csr1000v and write it to the var file or vault
outfile_csr_pub_ip='csr_pub_ip.json'
cmd_get_csr_pub_ip='aws ec2 describe-instances --instance-id' + " " + "{}".format(csr1000v_instance_id) + " " + '--query "Reservations[*].Instances[*].PublicIpAddress"'
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

from netmiko import ConnectHandler
key_file=name
ip = "192.168.1.1 255.255.255.0"

#connection = netmiko.ConnectHandler(ip="54.225.2.16", device_type="cisco_ios", username="ec2-user", key_file="kp.pem")

csr = {
    "device_type": "cisco_ios",
    "ip": csr_pub_ip,
    "username": "ec2-user",
    "key_file": name,
}

net_connect = ConnectHandler(**csr)
net_connect.enable()

output = net_connect.send_config_set("host csr1000v")
print(output)

output = net_connect.send_command("end")
print(output)

output = net_connect.send_command("wr")
print(output)

output = net_connect.send_command("show ip int brief")
print(output)

output = net_connect.send_config_set("iox")
print(output)

output = net_connect.send_command("end")
print(output)

output = net_connect.send_command("wr")
print(output)

output = net_connect.send_command("show iox-service")
print(output)

output = net_connect.send_command("guestshell")
print(output)

output = net_connect.send_config_set("app-hosting appid guestshell")
print(output)


config_commands= [ 'interface VirtualPortGroup1',
                   'ip address 192.168.1.1 255.255.255.0',
                   'no shut']
output = net_connect.send_config_set(config_commands)
print(output)
output = net_connect.send_command("end")
print(output)


config_commands= [ 'app-hosting appid guestshell',
                   'vnic gateway1 virtualportgroup 0 guest-interface 0 guest-ipaddress 192.168.1.2 netmask 255.255.255.0 gateway 192.168.1.1 name-server 8.8.8.8']
output = net_connect.send_config_set(config_commands)
print(output)

output = net_connect.send_command("end")
print(output)

config_commands= [ 'interface VirtualPortGroup0',
                   'ip nat inside',
                   'exit',
                   'interface GigabitEthernet1',
                   'ip nat outside',
                   'exit',
                   'ip access-list extended NAT-ACL',
                   'permit ip 192.168.1.0 0.0.0.255 any',
                   'exit',
                   'ip nat inside source list NAT-ACL interface GigabitEthernet1 overload',
                   'end']

output = net_connect.send_config_set(config_commands)
print(output)
output = net_connect.send_command("end")
print(output)

config_commands= ['int gig 2',
                  'ip address 10.10.20.100 255.255.255.0',
                  'no shut']

output = net_connect.send_config_set(config_commands)
print(output)
output = net_connect.send_command("end")
print(output)


