#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export SSH_TOKEN=$SSH_TOKEN
export TE_GROUP=$TE_GROUP
export AWS_KEY_ID=lab-kops/((Access_key_ID.Access_key))
export AWS_KEY=lab-kops/((Secret_access_key.Secret_access_key))
print $AWS_KEY_ID
