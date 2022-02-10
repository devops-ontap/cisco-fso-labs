#!/usr/bin/env bash
# Upload chrome extension to Chrome Web Store
# Usage: chrome-upload.sh CLIENT_ID CLIENT_SECRET REFRESH_TOKEN APP_ID FILENAME

CLIENT_ID=$1
CLIENT_SECRET=$2
TOKEN=$3
APP_ID=$4
FILENAME=$5

# Get the access token
TOKEN_JSON=`curl "https://accounts.google.com/o/oauth2/token" -d "client_id=$CLIENT_ID&client_secret=$CLIENT_SECRET&refresh_token=$TOKEN&grant_type=refresh_token&redirect_uri=urn:ietf:wg:oauth:2.0:oob"`

# Verify no error is returned
JSON_VALUE=$(echo "$TOKEN_JSON" | jq -r '.error')
if [ "$JSON_VALUE" != "null" ]
then
    echo "Error returned: $TOKEN_JSON"
    exit 1
fi

# Get the access token
JSON_VALUE=$(echo "$TOKEN_JSON" | jq -r '.access_token')
if [ "$JSON_VALUE" == "" ]
then
    echo "Unable to find access_token in $TOKEN_JSON"
    exit 1
fi
ACCESS_TOKEN=$JSON_VALUE

# Upload the file
echo "Using access token $ACCESS_TOKEN to update extension"
UPLOAD_RESP=`curl \
    -H "Authorization: Bearer $ACCESS_TOKEN"  \
    -H "x-goog-api-version: 2" \
    -X PUT \
    -T $FILENAME \
    -v "https://www.googleapis.com/upload/chromewebstore/v1.1/items/$APP_ID"`

echo $UPLOAD_RESP

# Print potential errors
if [[ "$UPLOAD_RESP" == *"error"* ]] || [ "$UPLOAD_RESP" == "" ]
then
    echo "Error returned: $UPLOAD_RESP"
    exit 1
fi

echo "Publishing Chrome extension"
PUBLICH_RESP=`curl \
-H "Authorization: Bearer $ACCESS_TOKEN"  \
-H "x-goog-api-version: 2" \
-H "Content-Length: 0" \
-X POST \
-v \
https://www.googleapis.com/chromewebstore/v1.1/items/$APP_ID/publish`

echo $PUBLICH_RESP

# Print potential errors
if [[ "$PUBLICH_RESP" == *"error"* ]] || [ "$PUBLICH_RESP" == "" ]
then
    echo "Error returned: $PUBLICH_RESP"
    exit 1
fi

echo "Chrome extension upload finished"
exit 0
