#!/bin/sh
export AWS_PAGER=""
#installing hvac
pip3 install hvac
pip3 install "hvac[parser"
cp config ~/.aws
python3 aws-deploy-env-train.py

