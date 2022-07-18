#!/bin/sh
cd input
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
APPD_SECRET=$(vault kv get --field=key concourse/cisco-fso-labs/appd-secret)
export APPD_SECRET=$APPD_SECRET
python3 get_appd_token_v2.py