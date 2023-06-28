FROM alpine:3.18

RUN apk update && apk upgrade
RUN apk add --no-cache curl chromium vim nodejs=18.16.1-r0 yarn=1.22.19-r0

RUN yarn global add @angular/cli


ENV CHROME_BIN=/usr/bin/chromium-browser

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app/

COPY . .

RUN yarn install