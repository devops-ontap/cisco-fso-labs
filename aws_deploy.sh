#!/bin/sh
export AWS_PAGER=""
cp config ~/.aws
python3 aws-deploy-env-train_vault.py

