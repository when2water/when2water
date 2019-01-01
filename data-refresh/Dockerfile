# https://stackoverflow.com/a/47960145
FROM alpine:3.6

RUN apk add --no-cache python3

WORKDIR /app
COPY . .

# copy crontabs for root user
COPY cronjobs /etc/crontabs/root

# start crond with log level 8 in foreground, output to stderr
CMD ["crond", "-f", "-d", "8"]
