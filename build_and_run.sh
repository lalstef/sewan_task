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
	sewan:latest