#!/bin/sh
# disable filename globbing
set -f
echo Content-type: text/plain
echo
echo "HTTP + Moonshot authentication as user '$REMOTE_USER' with the following attributes (in JSON format):"
echo $GSS_NAME_ATTRS_JSON
