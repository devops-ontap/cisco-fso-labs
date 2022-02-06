#!/usr/bin/env bash

while read ins_id; do
  aws ec2 terminate-instances --instance-ids $ins_id | echo "error terminating ${ins_id}"
done < instids.txt