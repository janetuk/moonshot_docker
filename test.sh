#!/usr/bin/env bash
set -e
trap "echo 'Something went wrong!!!!'" ERR

echo "-----Running Moonshot tests ------"
docker-compose down -t 0
docker-compose up --build -d

echo "-----------------Importing User Credentials-----------------------"
docker-compose exec -e DISPLAY client dbus-launch moonshot-webp /config/user_credentials.xml

echo "-----------------Testing SSH-----------------------"
docker-compose exec -e DISPLAY client dbus-launch ssh -o StrictHostKeyChecking=no moonshot@sshserver echo "SSH authenticated with moonshot"

echo "-----------------Testing Apache --------------------"
docker-compose exec -e DISPLAY client dbus-launch curl --negotiate -u ":" http://httpserver/protected/hello.cgi

docker-compose stop -t 0
