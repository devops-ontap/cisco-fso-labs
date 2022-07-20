
import json, requests, os
from intersight_auth import IntersightAuth

#import environment variables
api_key_id = os.getenv('keyid')
secret = os.getenv('secret')


#Configure Intersight API token and start finding all devices with a non-active or expiring soon contract status
AUTH = IntersightAuth(
    secret_key_filename='SecretKey.txt',
    api_key_id=api_key_id
)

#Get Physical Summaries

json_body = {
    "request_method": "GET",
    "resource_path": (
        #'https://intersight.com//api/v1/network/VlanPortInfos'
        #'https://intersight.com/api/v1/storage/PhysicalDisks'
        #'https://intersight.com/api/v1/compute/PhysicalSummaries'
    )
}

RESPONSE = requests.request(
    method=json_body['request_method'],
    url=json_body['resource_path'],
    auth=AUTH
)

print(RESPONSE.text)
print(RESPONSE.json)

RESPONSE_JSON = RESPONSE.json
print(RESPONSE_JSON)

'''

#write the token to a json file called data.json
outfile = 'intersight-payload.json'
with open(outfile, 'w') as my_file:
    my_file.write(RESPONSE_JSON)
my_file.close()
'''