#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
rm -rf __pycache__

curl -O
scp -i *.pem


python3 configure_appd.py
