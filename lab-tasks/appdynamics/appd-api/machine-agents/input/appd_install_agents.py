#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko
from subprocess import call, check_output

#Install the Agent
#See if  you can pull the pem from vault

#from os import environ
os.environ.get('SSHKEY')
os.environ.get('VAULT_ADDR')

os.chmod("sshkey.pem", 400)
os.chmod("appdynamics-machine-agent-22.2.0.3282.x86_64.rpm", 777)

private_key = 'sshkey.pem'
key = paramiko.RSAKey.from_private_key_file(private_key)
username='ubuntu'
hostfile='hostfile'
commandfile='appd-commandfile'

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
        con.connect(hostname=device, username=username, allow_agent=False, pkey=key, port=22, timeout=60)
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



