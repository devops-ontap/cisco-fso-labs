import json
import requests
from intersight_auth import IntersightAuth

#Configure Intersight API token and start finding all devices with a non-active or expiring soon contract status
AUTH = IntersightAuth(
    secret_key_filename='SecretKey.txt',
    api_key_id='614a0b357564612d33f7f416/614a0b357564612d33f7f41a/628e66187564612d3335170d'
)
#print(AUTH)



#Get Physical Summaries

json_body = {
    "request_method": "GET",
    "resource_path": (
        'https://intersight.com/api/v1/compute/PhysicalSummaries'
    )
}

RESPONSE = requests.request(
    method=json_body['request_method'],
    url=json_body['resource_path'],
    auth=AUTH
)

print(RESPONSE.text)


