Python program to convert
# JSON file to CSV

import json
import csv

# Opening JSON file and loading the data
# into the variable data

with open('item.json') as json_file:
    data = json.load(json_file)
 
# now we will open a file for writing
out_file = open('cred.csv', 'w')
 
# create the csv writer object
csv_writer = csv.writer(out_file)
 
# Counter variable used for writing
# headers to the CSV file
count = 0
 
for item in in_file:
    if count == 0:
 
        # Writing headers of CSV file
        header = item.keys()
        csv_writer.writerow(header)
        count += 1
 
    # Writing data of CSV file
    csv_writer.writerow(item.values())
 
out_file.close()