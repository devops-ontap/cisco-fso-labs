#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
cp config ~/.aws
python3 aws-deploy-env-train.py

