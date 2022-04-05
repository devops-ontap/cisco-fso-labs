#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
export TE_GROUP=$TE_GROUP
export AWS_KEY_ID=((Access_key_ID.Access_key))
export AWS_KEY=((Secret_access_key.Secret_access_key))
print $AWS_KEY_ID
