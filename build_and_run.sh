docker \
	build \
	--file deployment/Dockerfile \
	--tag sewan \
	--build-arg email_backend=$1 \
	--build-arg http_backend=$2 \
	. \
&& \
docker run \
	--publish 8003:8003 \
	--detach \
	--env SMTP_HOST="${SMTP_HOST}" \
	--env SMTP_PORT="${SMTP_PORT}" \
	--env SMTP_USERNAME="${SMTP_USERNAME}" \
	--env SMTP_PASSWORD="${SMTP_PASSWORD}" \
	sewan:latest