#!/bin/bash
#

while read line
for project in `cat output.txt`; do
echo $project
curl -D- -u user:pass -X POST --data "{\"fields\":{\"project\":{\"key\":\"TECH\"},\"parent\":{\"key\":\"$project\"},\"summary\":\"TestChargenNr\",\"description\":\"some description\",\"issuetype\":{\"name\":\"Sub-task\"},\"customfield_10107\":{\"id\":\"10400\"}}}" -H "Content-Type:application/json" https://jira.company.com/rest/api/latest/issue/

 done
xargs -I{} curl "xyz.com/v1/"{} <file

#xargs -I{} curl "curl url -d '{"interval": 300, "agents": [{"agentId":"{}], "testName": "agent to server", "server": "www.thousandeyes.com"}' -H "Content-Type: application/json" --header "Authorization: $token <agents