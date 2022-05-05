import credentials
from intersight.api import server_api
from intersight.rest import ApiException
from intersight.model.server_profile import ServerProfile
from intersight.model.mo_base_mo_relationship import MoBaseMoRelationship

# Variables. Change accordingly
org_moid = '5ddee8bb6972652d31030baf'

# Authenticate
api_client = credentials.config_credentials()

#### Sample JSON Payload for Reference ####
"""
{
    "Name": "server_profile_test",
    "Organization":
    {
        "ObjectType": "organization.Organization",
        "Moid": "5ddee8bb6972652d31030baf"
    },
    "TargetPlatform": "Standalone"
}

"""

def create_server_profile(api_client):
    api_instance = server_api.ServerApi(api_client)
    try:
        api_response = api_instance.create_server_profile(server_profile)
        return api_response
    except ApiException as e:
        print("Exception when calling ServerApi->create_server_profile: %s\n" % e)

#### Org Definition Payload ###

ass_obj = MoBaseMoRelationship(
    moid=org_moid,
    object_type="organization.Organization",
    class_id="mo.MoRef"
)

# SP Definition

server_profile = ServerProfile(
    name="Server_Profile_from_SDK",
    organization=ass_obj,
    target_platform="Standalone"
)

create_server_profile(api_client)