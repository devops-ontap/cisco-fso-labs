#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()
import requests

#The AppD secret is passed in via Env Var which is injected into the build container via the pipeline
#import the env vars and logon to vault to get the secret and then use it to run this command and write the output to the vault
secret = os.getenv('APPD_SECRET')


url = "https://cisco-apipartnertraininglab.saas.appdynamics.com/auth/v1/oauth/token"
payload='grant_type=client_credentials&client_id=fsolab4%40cisco-apipartnertraininglab&client_secret=' + secret
print(payload)
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)


token_json = response.json()
TOKEN = token_json['access_token']
print(TOKEN)



#write the token to a json file called data.json
outfile = 'token.json'
with open(outfile, 'w') as my_file:
    my_file.write(TOKEN)
my_file.close()


#write the appd oath token returned from the api call to the vault

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath"

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')

test='12345'

headers = CaseInsensitiveDict()
headers = {"X-Vault-Token":VAULT_TOKEN}
headers = {"Content-Type: application/json"}
data = '{"data":{"token":TOKEN}'
resp = requests.post(url=url,data=data)
print(resp.text)
print(type(resp.text))



import requests
from requests.structures import CaseInsensitiveDict

url = "http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath"

headers = CaseInsensitiveDict()
headers["X-Vault-Token"] = "s.s1UuURYXGclHOSQz5MhTrdWS"
headers["Content-Type"] = "application/json"

#data = '{"token":"eyJraWQiOiJiN2UzOTg1OS1iOTE0LTRiNzItYjU3NS0wNDExYTQ2NTU4YzUiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJBcHBEeW5hbWljcyIsImF1ZCI6IkFwcERfQVBJcyIsImp0aSI6IlNfVl9OaXFRa2I0c1lKOFQ5TWNBZWciLCJzdWIiOiJmc29sYWI0IiwiaWRUeXBlIjoiQVBJX0NMSUVOVCIsImlkIjoiY2NlNmI5Y2YtMWU4NC00MTI1LWI4MWYtMDhiMDU5MTEwNTE5IiwiYWNjdElkIjoiNDEzMTk1MmItNmNhOC00NWUyLWFiYmQtNTcyMGYxZmQ2YjhjIiwidG50SWQiOiI0MTMxOTUyYi02Y2E4LTQ1ZTItYWJiZC01NzIwZjFmZDZiOGMiLCJhY2N0TmFtZSI6ImNpc2NvLWFwaXBhcnRuZXJ0cmFpbmluZ2xhYiIsInRlbmFudE5hbWUiOiJjaXNjby1hcGlwYXJ0bmVydHJhaW5pbmdsYWIiLCJmbW1UbnRJZCI6bnVsbCwiYWNjdFBlcm0iOltdLCJyb2xlSWRzIjpbXSwiaWF0IjoxNjUwOTg4OTAzLCJuYmYiOjE2NTA5ODg3ODMsImV4cCI6MTY1MTA3NTMwMywidG9rZW5UeXBlIjoiQUNDRVNTIn0.XzcN_mV2dWEM4TP4LSyzbAQ0FkmhZMaNsXpCeidrn51DLOwY7Q2lx7T47-BKRK_U4XzodbjYAotk_HTkzfqG-1Kzd8Pe2_rIc3Gbc833if__0M-N4VONHXweSKcqRTXqIMUAoU_2nP_UgEXP8q8iENBcAFEx3mN7cYLmdiooopxlUdng3l8pNotrS3CcfJzknFnkSN3Jc5YlGUhdaHRYiumW5sgiKhWfny34SJzLpEbAAgWppk6Lp_knBeZfK2IQW3GW64qWNWN_xDVKuEJDYmGkuinerWJ3uz8bVYEFN3vHoWDxLxf2sQY6GHz0vSU-qxw85MM4ul_dBZh0ETbFKFUjiLScixXJvZYb1H0jrgBmVMg7iwsgOntY3-XLc_8WiSUmQCxxs43N21908sgsDtKnagsC0OrRheWC0G1lnaMkKRvr0lncBX56VPLkuf3v06e2LJcNkdrIptsbhQAJcV31_lqjiFnsRgA8BEHWErkRCIvFcj85D9gkICuW3Adn"}'
TOKEN='eyJraWQiOiJiN2UzOTg1OS1iOTE0LTRiNzItYjU3NS0wNDExYTQ2NTU4YzUiLCJhbGciOiJSUzUxMiJ9.eyJpc3MiOiJBcHBEeW5hbWljcyIsImF1ZCI6IkFwcERfQVBJcyIsImp0aSI6IlNfVl9OaXFRa2I0c1lKOFQ5TWNBZWciLCJzdWIiOiJmc29sYWI0IiwiaWRUeXBlIjoiQVBJX0NMSUVOVCIsImlkIjoiY2NlNmI5Y2YtMWU4NC00MTI1LWI4MWYtMDhiMDU5MTEwNTE5IiwiYWNjdElkIjoiNDEzMTk1MmItNmNhOC00NWUyLWFiYmQtNTcyMGYxZmQ2YjhjIiwidG50SWQiOiI0MTMxOTUyYi02Y2E4LTQ1ZTItYWJiZC01NzIwZjFmZDZiOGMiLCJhY2N0TmFtZSI6ImNpc2NvLWFwaXBhcnRuZXJ0cmFpbmluZ2xhYiIsInRlbmFudE5hbWUiOiJjaXNjby1hcGlwYXJ0bmVydHJhaW5pbmdsYWIiLCJmbW1UbnRJZCI6bnVsbCwiYWNjdFBlcm0iOltdLCJyb2xlSWRzIjpbXSwiaWF0IjoxNjUwOTg4OTAzLCJuYmYiOjE2NTA5ODg3ODMsImV4cCI6MTY1MTA3NTMwMywidG9rZW5UeXBlIjoiQUNDRVNTIn0.XzcN_mV2dWEM4TP4LSyzbAQ0FkmhZMaNsXpCeidrn51DLOwY7Q2lx7T47-BKRK_U4XzodbjYAotk_HTkzfqG-1Kzd8Pe2_rIc3Gbc833if__0M-N4VONHXweSKcqRTXqIMUAoU_2nP_UgEXP8q8iENBcAFEx3mN7cYLmdiooopxlUdng3l8pNotrS3CcfJzknFnkSN3Jc5YlGUhdaHRYiumW5sgiKhWfny34SJzLpEbAAgWppk6Lp_knBeZfK2IQW3GW64qWNWN_xDVKuEJDYmGkuinerWJ3uz8bVYEFN3vHoWDxLxf2sQY6GHz0vSU-qxw85MM4ul_dBZh0ETbFKFUjiLScixXJvZYb1H0jrgBmVMg7iwsgOntY3-XLc_8WiSUmQCxxs43N21908sgsDtKnagsC0OrRheWC0G1lnaMkKRvr0lncBX56VPLkuf3v06e2LJcNkdrIptsbhQAJcV31_lqjiFnsRgA8BEHWErkRCIvFcj85D9gkICuW3Adn'

data = '{"token": }'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)


'''
deployment_status = 'status'
data = f'{ "ref": "cd-pipeline", "variables": [ {"key": "STAGE", "value": "CD"}, {"key": "DEPLOYMENT_STATUS", "value": "{deployment_status}"} ] }'

import json

deployment_status = 'failed'
data = {"ref": "cd-pipeline", "variables": [ {"key": "STAGE", "value": "CD"}, {"key": "DEPLOYMENT_STATUS", "value": deployment_status} ] }

print(json.dumps(data))

'''