#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict

#Download the TE Agent
#Scp the Agent to the Ubuntu
#Install the Agent
private_key='us-east-2a.pem'
key = paramiko.RSAKey.from_private_key_file(private_key)
username='ubuntu'
#host='3.142.196.185'

hostfile='hostfile'
commandfile='commandfile'

# Opens files in read mode
f1 = open(hostfile,"r")
f2 = open(commandfile,"r")

# Creates list based on f1 and f2
devices = f1.readlines()
commands = f2.readlines()

for device in devices:
    device = device.rstrip()
    for command in commands:
        con = paramiko.SSHClient()
        con.load_system_host_keys()
        con.connect(device, username=username, allow_agent=False, pkey=key)
        print("="*50, command, "="*50)
        stdin, stdout, stderr = con.exec_command(command, get_pty=True)
        print(stdout.read().decode())
        err = stderr.read().decode()
        time.sleep(3)
        if err:
            print(err)
        f1.close()
        f2.close()
con.close()
