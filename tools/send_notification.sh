#!/bin/bash

notification="Money have been withdrawn from your bank account."
if [ "$1" != "" ]; then
	notification=$1
fi

curl \
    --request POST \
    --header "Content-Type: application/json" \
    --data "{\"notification\":\"${notification}\"}" \
    http://0.0.0.0:8003/api/v1.0/notification