FROM alpine:3.16

WORKDIR /home/src/web

RUN apk update
RUN apk add --no-cache bash
RUN apk add --no-cache python3-dev
RUN apk add --no-cache py3-pip
RUN apk add --no-cache musl-dev
RUN apk add --no-cache gcc g++

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

RUN chmod +x /web/server-entrypoint.sh
RUN chmod +x /web/worker-entrypoint.sh