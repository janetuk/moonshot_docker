#!/bin/env bash

for IMAGE in apc trustrouter sshserver httpserver client
do
    docker tag moonshot_docker_$IMAGE jiscmoonshot/$IMAGE
    docker push jiscmoonshot/$IMAGE
done
docker tag moonshot_docker_idp1 jiscmoonshot/idp
docker push jiscmoonshot/idp

