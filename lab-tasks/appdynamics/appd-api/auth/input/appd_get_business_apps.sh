#!/bin/sh
cd input
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
APPD_OATH_TOKEN=$(vault kv get --field=token concourse/cisco-fso-labs/appd-oath)
export APPD_OATH_TOKEN=$APPD_OATH_TOKEN
python3 appd_get_business_apps.py