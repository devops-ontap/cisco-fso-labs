#!/bin/sh
export AWS_PAGER=""
#installing hvac
cp config ~/.aws
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
python3 aws-deploy-env-train.py

