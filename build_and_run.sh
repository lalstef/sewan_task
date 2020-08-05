docker \
	build \
	-f deployment/Dockerfile \
	-t sewan \
	. \
&& \
docker run \
	--publish 8003:8003 \
	--detach \
	--restart=always \
	sewan:latest