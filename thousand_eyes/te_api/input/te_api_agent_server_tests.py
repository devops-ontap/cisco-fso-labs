
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
for key in test_dict:
    collect[key['agentId']]
for k in (dict(collect)):
    print(k)

agents_file='agents.txt'
with open(agents_file, 'a+') as my_file:
    my_file.write(str(k) + "\n")


import subprocess, json
agentId = 'agents.txt'

with open("agents.txt") as file_in:
    lines = []
    for line in file_in:
        subprocess.run([
            'curl',
            '-X', 'POST',
            '-H', 'Content-Type: application/json',
            '-H', 'Accept: application/json',
            '-d', json.dumps({"interval": 300, "agents": [{"agentId": "{line}"}], "testName": "agent to server", "server": "www.thousandeyes.com"}),
            '-H', 'Authorization: $token',
            'https://api.thousandeyes.com/v6/instant/agent-to-server',
       ])
file(close)

'''
curl -i https://api.thousandeyes.com/v6/instant/agent-to-server \
-d '{ "agents": [ {"agentId": 113} ], "testName": "API Instant test", "server": "www.thousandeyes.com" }' \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
--header "Authorization: Bearer 2c55b646-eb53-4802-b3fe-0a02885ad516"





        subprocess.run([
            'curl',
            '-X', 'POST',
            '-H "Content-Type: application/json" 
            '-d json.dummps('{"interval": 300, "agents": [{"agentId": line}], "testName": "agent to server", "server": "www.thousandeyes.com"}),          
            'http://localhost.yxy',
        ])
        
        for var_name in k:
        
        #save this list of agentIds to a file then use it to run a loop over the file in order to set up tests
        #or just put this to a list in RAM and then loop over it to add all the agents to that particular test
        #curl url -d '{"interval": 300, "agents": [{"agentId": 438241}], "testName": "agent to server", "server": "www.thousandeyes.com"}' -H "Content-Type: application/json" --header "Authorization: Bearer token
        cmd='curl' + " " + url + " " + '' + -d '{"interval": 300, "agents": [{"agentId":' + agentId + '}],' + " " + '"testName": "agent to server", "server": "www.thousandeyes.com"}' -H "Content-Type: application/json" --header "Authorization: Bearer' + " " + token
        print(cmd)
        


output = check_output("{}".format(cmd), shell=True).decode().strip()
print("Output: \n{}\n".format(output))



curl https://api.thousandeyes.com/tests/agent-to-server/new.json \
-d '{"interval": 300, "agents": [{"agentId": 438241}], "testName": "agent to server", "server": "www.thousandeyes.com"}' \
-H "Content-Type: application/json" \
--header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"
'''