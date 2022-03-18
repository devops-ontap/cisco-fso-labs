#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko
from subprocess import call, check_output

#Install the Agent
#See if  you can pull the pem from vault

from os import environ
os.environ.get('SSHKEY')

sshkey = environ.get('SSHKEY')
print(sshkey)

with open('sshkey.pem', 'w+') as my_file:
    my_file.write(sshkey)

os.chmod("sshkey.pem", 400)

private_key = 'sshkey.pem'
key = paramiko.RSAKey.from_private_key_file(private_key)
username='ubuntu'
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
