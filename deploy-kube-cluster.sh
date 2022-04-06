#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
AWS_KEY_ID=$(vault kv get --field=AccessKeyId concourse/main/lab-kops)
AWS_SECRET=$(vault kv get --field=SecretAccessKey concourse/main/lab-kops)
echo $AWS_KEY_ID
echo $AWS_SECRET