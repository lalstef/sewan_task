# pull official base image
FROM python:3.8.1-slim-buster

ARG email_backend
ARG http_backend

# set work directory
WORKDIR .

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY deployment/start_server.sh start_server.sh

EXPOSE 8003:8003

# copy project
COPY app /app/

ENV EMAIL_BACKEND=${email_backend}
ENV HTTP_BACKEND=${http_backend}

ENTRYPOINT ["./start_server.sh"]