#!/bin/sh
sed 2,10d item.json > cred.cln.json
python3 con-cred-json-csv.py > item.csv
sed '/^$/d' item.csv > item.cln.csv



