import json, csv


infile='cred.cln.json'
outfile='cred-out.csv'


# Opening JSON file and loading the data
# into the variable data
with open('cred.cln.json') as json_file:
    data = json.load(json_file)

cred = data['note']
print(cred)