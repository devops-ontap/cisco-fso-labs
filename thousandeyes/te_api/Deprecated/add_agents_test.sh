#!/bin/bash
while read line
for project in `cat agents`; do
  echo $agentid
  curl https://api.thousandeyes.com/tests/agent-to-server/new.json \
  -d '{"interval": 300, "agents": [{"agentId": $agentid}], "testName": "API network test addition for www.thousandeyes.com", "server": "www.thousandeyes.com"}' \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 1d0acd78-a470-44ad-a6d6-0892ac2db441"
done