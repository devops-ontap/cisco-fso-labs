#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time
from subprocess import call, check_output
import scp
import paramiko
#Download the TE Agent
#Scp the Agent to the Ubuntu
#Install the Agent

private_key='us-east-2a.pem'
key = paramiko.RSAKey.from_private_key_file(private_key)
username='ubuntu'
host='3.145.46.2'

# connect to server
con = paramiko.SSHClient()
con.load_system_host_keys()
con.connect(host, username=username, allow_agent=False, pkey=key)

commands = [
    "pwd",
    "whoami",
    "export TERMINFO=/usr/lib/terminfo",
    "TERM=xterm",
    "sudo cp /tmp/install_thousandeyes.sh .",
    "sudo chmod a+x install_thousandeyes.sh",
    "sudo ./install_thousandeyes.sh -f -b vojylvcce2gwg4u0e1mcg000gn96h0tj",

]

# execute the commands
for command in commands:
    print("="*50, command, "="*50)
    stdin, stdout, stderr = con.exec_command(command, get_pty=True)
    print(stdout.read().decode())
    err = stderr.read().decode()
    time.sleep(3)
    if err:
        print(err)
client.close()
