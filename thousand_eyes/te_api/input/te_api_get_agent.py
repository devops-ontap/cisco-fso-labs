#!/usr/bin/env python
#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict

#Add Token to Vault
#token=call the token from vault

url = "https://api.thousandeyes.com/v6/agents.json"
token = "1d0acd78-a470-44ad-a6d6-0892ac2db441"
agents_file = 'agents.json'
#curl -o https://api.thousandeyes.com/v6/agents.json --header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"
cmd_1='curl -o' + " " + agents_file + " "  + url + " " + '--header' + " " '"' + 'Authorization: Bearer' + " " + token + '"'
output = check_output("{}".format(cmd_1), shell=True).decode().strip()
print("Output: \n{}\n".format(output))

#Require to Loop over the embedded dictionaries in the list of agents

with open(agents_file) as access_json:
    read_content = json.load(access_json)
    question_content = read_content['agents']
    question_data=question_content[0]
    agentId=question_data['agentId']
    print(agentId)
    agentId=agentId









'''
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {token}"


resp = requests.get(url, headers=headers)

print(resp.status_code)


#Filter Output to get the Agent ID


#Open json file to write output
# read file
with open('agents.json', 'r') as myfile:
    data=myfile.read()

# parse file
obj = json.loads(data)
print(obj)

# show values
#print("usd: " + str(obj['usd']))

outfile_agents='agents.json'
with open(outfile_agents, 'w') as my_file:
    my_file.write(resp)
with open (outfile_agents) as access_json:
    read_content = json.load(access_json)
    print(read_content)

'''