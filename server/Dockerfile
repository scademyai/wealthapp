FROM python:3.5.10-alpine

RUN apk update && apk upgrade
RUN apk add --no-cache curl postgresql-libs vim && \
    apk add --no-cache --virtual .build-deps gcc g++ musl-dev postgresql-dev libffi-dev

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

RUN python -m venv .venv

COPY . .

RUN source .venv/bin/activate && pip install -r requirements.txt
