#!/bin/sh
# disable filename globbing
set -f
echo Content-type: text/plain
echo
echo "HTTP + Moonshot authentication as $REMOTE_USER."
