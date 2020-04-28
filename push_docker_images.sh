#!/bin/env bash
for IMAGE in apc trustrouter sshserver httpserver client idp
do
    docker push jiscmoonshot/$IMAGE
done

