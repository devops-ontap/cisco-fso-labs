import json
import requests

from intersight_auth import IntersightAuth

#Get user friendly information from the deviceid
def getModelAndDeviceName(serial,devicetype):
    if devicetype == "CiscoUcsFI":
        json_body = {
            "request_method": "GET",
            "resource_path": (
                    'https://intersight.com/api/v1/network/ElementSummaries?$filter=Serial eq ' + serial
            )
        }
    elif devicetype == "CiscoUcsServer":
        json_body = {
            "request_method": "GET",
            "resource_path": (
                    'https://intersight.com/api/v1/compute/PhysicalSummaries?$filter=Serial eq ' + serial
            )
        }

    RESPONSE = requests.request(
        method=json_body['request_method'],
        url=json_body['resource_path'],
        auth=AUTH
    )
   
    affectedDevice = RESPONSE.json()["Results"]
    for r in affectedDevice:
        return(r['Model'] + ", " + r['Name'])

#Get all devices with a contract status not set to active (currently not covered or expiring soon)
def getExpiringOrInactiveContracts():
    print("Serial #      Status        Expiration Date        Model         Name")
    print("---------------------------------------------------------------------------------------")

    json_body = {
        "request_method": "GET",
        "resource_path": (
                'https://www.intersight.com/api/v1/asset/DeviceContractInformations?$filter=ContractStatus ne \'Active\''
        )
    }

    RESPONSE = requests.request(
        method=json_body['request_method'],
        url=json_body['resource_path'],
        auth=AUTH
    )

    affectedDevice = RESPONSE.json()["Results"]
    for r in affectedDevice:
        try:
           print(r['DeviceId'],",",r['ContractStatus'],",",r['ServiceEndDate'],",",getModelAndDeviceName(r['DeviceId'],r['DeviceType']))
        except:
           print("")

#Configure Intersight API token and start finding all devices with a non-active or expiring soon contract status        
AUTH = IntersightAuth(
    secret_key_filename='SecretKey.txt',
    api_key_id='614a0b357564612d33f7f416/614a0b357564612d33f7f41a/628e66187564612d3335170d'
    )

getExpiringOrInactiveContracts()
