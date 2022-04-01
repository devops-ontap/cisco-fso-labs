#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, paramiko, urllib3
import pandas as pd
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
token = os.getenv('TE_OATHTOKEN')
token = '1d0acd78-a470-44ad-a6d6-0892ac2db441'
test_name = 'test-33'
url = "https://api.thousandeyes.com/v6/agents.json"
payload={}
headers = {'Authorization': 'Bearer ' + token}
agent_response = requests.request("GET", url, headers=headers, data=payload)

agent_list_json = agent_response.json()
agent_list = agent_list_json['agents']
list_of_dictionaries = agent_list
sought_value = "Enterprise"
found_values = []
for dictionary in list_of_dictionaries:
    if (dictionary["agentType"] == "Enterprise"):
        found_values.append(dictionary)
print(found_values)

empty_list=[]
for item in found_values:
    agentId=item['agentId']
    print(agentId)
    empty_list.append({'agentId': agentId})
print(empty_list)

#For some reason the API will only see to accept the list of agents like this.....
#The expected format of the list of agents, is cumbersome because it requires you to create a list of dictionaries instead of just using the list of agentIDs
#agents = [{'agentId': '443526'}, {'agentId': '443531'}]
url='https://api.thousandeyes.com/v6/tests/agent-to-server/new.json'
payload = {'interval': '300', 'agents': empty_list, 'testName': 'test-60', 'port': '80', 'server': 'www.thousandeyes.com','alertsEnabled': '0'}
header = {'content-type': 'application/json', 'authorization': 'Bearer ' + token}
r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
print(r)