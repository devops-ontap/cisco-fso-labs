#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, pycurl, requests
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict

#Add Token to Vault
#token=call the token from vault


#curl https://api.thousandeyes.com/v6/agents.json --header "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"
url = "https://api.thousandeyes.com/v6/agents.json"
#The token var should be passed in via vault
token = "1d0acd78-a470-44ad-a6d6-0892ac2db441"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer {token}"


resp = requests.get(url, headers=headers)

print(resp.status_code)


''''
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