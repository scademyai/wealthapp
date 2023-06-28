FROM python:3.11.4-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache curl git postgresql-libs vim 
RUN apk add --no-cache --virtual .build-deps gcc g++ postgresql-dev musl-dev

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt
