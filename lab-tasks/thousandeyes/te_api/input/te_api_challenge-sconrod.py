#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
token = os.getenv('TE_OATHTOKEN')
url = "https://api.thousandeyes.com/v6/tests.json"
payload={}
headers = {'Authorization': 'Bearer ' + token}
agent_response = requests.request("GET", url, headers=headers, data=payload)
print(agent_response)

test_list_json = agent_response.json()
#This brings back all test types. Get just agent-to-server tests
test_list = test_list_json['test']
list_of_dictionaries = test_list
sought_value = "agent-to-server"
found_values = []
for dictionary in list_of_dictionaries:
    if (dictionary["type"] == "agent-to-server"):
        found_values.append(dictionary)
print(found_values)
test_list_json = agent_response.json()
#This brings back all test types. Get just agent-to-server tests
test_list = test_list_json['test']
list_of_dictionaries = test_list
sought_value = "testName"
found_values = []
for dictionary in list_of_dictionaries:
    if (dictionary["testName"] == "sconrod-test"):
        found_values.append(dictionary)
print(found_values)
empty_list=[]
for item in found_values:
    testId=item['testId']
    print(testId)

#tests/agent-to-server/2994789/update.json
url='https://api.thousandeyes.com/v6/tests/agent-to-server/2994789/update.json'
payload = {'bandwidthMeasurements': '1'}
header = {'content-type': 'application/json', 'authorization': 'Bearer ' + token}
r = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
print(r)

