#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
#logging into vault with the lab account token to get the appd-secret and put to env var for python
vault login --no-print $SSH_TOKEN
APPD_SECRET=$(vault kv get --field=key concourse/cisco-fso-labs/appd-secret)
export APPD_SECRET=$APPD_SECRET
#python can now connect to appd to generate the bearer token and set to var
python3 get_appd_token.py
vault kv put concourse/cisco-fso-labs/appd-oath token=@token.json
vault kv get --field=token concourse/cisco-fso-labs/appd-oath