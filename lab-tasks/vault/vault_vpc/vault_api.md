#
token='enter your token here'
curl -H "X-Vault-Token: $token" -X GET http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/us-east-2a/vpcid | jq

Reading:
=========
https://www.criticaldesign.net/post/how-to-get-started-with-hashicorp-vault-for-secrets-management-in-your-devops-pipeline-part-3

Writing:
========

curl --header "X-Vault-Token: TOKEN" --request POST --data @payload.json http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath


#This works...
curl --request POST --header "X-Vault-Token:" --header "Content-Type: application/json" --data '{"token":"INSERT_BEARER_TOKEN"}' --url http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath


Tested and Works
curl --request POST --header "X-Vault-Token: TOKEN" --header "Content-Type: application/json" --data '{"token":"testing"}' --url http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath

curl --request POST --header "X-Vault-Token: TOKEN" --header "Content-Type: application/json" --data '{"token":"{}""}' --url http://vault.devops-ontap.com:8200/v1/concourse/cisco-fso-labs/appd-oath