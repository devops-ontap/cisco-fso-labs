import json, os, requests
from intersight_auth import IntersightAuth

#import environment variables
api_key_id = os.getenv('keyid')
secret = os.getenv('secret')
print("printing the type")
print(type(api_key_id))

#dump the secret to a file here..

#Configure Intersight API token and start finding all devices with a non-active or expiring soon contract status
AUTH = IntersightAuth(
    secret_key_filename=SecretKey.txt,
    api_key_id=api_key_id
)
print(api_key_id)
print(AUTH)

#Get Physical Summaries

json_body = {
    "request_method": "GET",
    "resource_path": (
        'https://intersight.com/api/v1/compute/RackUnits'
    )
}

RESPONSE = requests.request(
    method=json_body['request_method'],
    url=json_body['resource_path'],
    auth=AUTH
)

print(RESPONSE.text)



