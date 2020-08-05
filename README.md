# Sewan Task

# Installation
```
git clone git@github.com:lalstef/sewan_task.git
```

## Environment variables
The following environment variables needs to be set:

```
SMTP_HOST
SMTP_PORT
SMTP_USERNAME
SMTP_PASSWORD
```

# Run

The script builds a docker image and starts a docker container with port 8003 exposed.

```
cd sewan
./build_and_run.sh admin@example.com http://api.example.com/test/
```


# Usage
```
curl \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"notification":"Money have been withdrawn from your bank account."}' \
    http://0.0.0.0:8003/api/v1.0/notification
```

or you could use the command line tool:

```
tools/send_notification.sh
tools/send_notification.sh <notification>
```

# Running Tests
