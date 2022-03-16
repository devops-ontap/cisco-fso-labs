#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko
import pandas as pd
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict

#Add Token to Vault
#token=call the token from vault
url = "https://api.thousandeyes.com/v6/agents.json"
# Get environment variables
token = os.getenv('TE_OATHTOKEN')
agents_file = 'agents.json'
#example:
#curl -o https://api.thousandeyes.com/v6/agents.json --header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"
cmd_1='curl -o' + " " + agents_file + " "  + url + " " + '--header' + " " '"' + 'Authorization: Bearer' + " " + token + '"'
print(cmd_1)
output = check_output("{}".format(cmd_1), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#Require to Loop over the embedded dictionaries in the list of agents
with open(agents_file) as access_json:
    read_content = json.load(access_json)
    print(type(read_content))
    question_content = read_content['agents']
    print(type(question_content))

#use a for loop to iterate through each dictionary in the list and chek if it contains the sought value
list_of_dictionaries = question_content
sought_value = "Enterprise"
found_values = []
for dictionary in list_of_dictionaries:
    if (dictionary["agentType"] == "Enterprise"):
        found_values.append(dictionary)
print(found_values)

from collections import defaultdict
test_dict = found_values
collect = defaultdict(dict)

# at this moment, 'key' becomes every dict of your list of dict
agents_file='agents.txt'
for key in test_dict:
    collect[key['agentId']]
for k in (dict(collect)):
    print(k)

with open('agents.txt', 'w') as file:
    file.write('\n'.join(str(key['agentId']) for key in test_dict))


import requests
with open("agents.txt") as file:
    lines = []
    for line in file:
        subprocess.call([
            'curl',
            '-X', 'POST',
            '-H', 'Content-Type: application/json',
            '-H', 'Accept: application/json',
            '-d', json.dumps({"interval": 300, "agents": [{"agentId": "{}".format(line)}], "testName": "agent to server 1-", "server": "www.thousandeyes.com"}),
            '-H', "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441",
            'https://api.thousandeyes.com/v6/instant/agent-to-server'
       ])

