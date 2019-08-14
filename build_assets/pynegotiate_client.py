#!/usr/bin/env python
# Author: Alejandro Perez
# Contact: alex@um.es

"""Small script to perform the client side of an HTTP Negotiate (aka GSS-API) authentication.
If successful, it dumps the data of the accessed resource.
"""

import time
import socket
import argparse
import sys
import urlparse
import base64
import httplib
import gssapi

# parse the options
parser = argparse.ArgumentParser()
parser.add_argument('url',
    help='The url of the protected resource (including the http:// or https://).')
parser.add_argument('-i', '--iterations', type=int, default=1,
    help='The number of times the script will request the resource. For stress tests.')
parser.add_argument('-d', '--delay', type=float, default=0.0,
    help='The delay between different requests within the same iteration.')
parser.add_argument('-w', '--wait', type=float, default=0.0,
    help='The delay between different iterations.')
parser.add_argument('-v', '--verbose', action='store_true',
    help='Show sent/received GSS API tokens.')
args = parser.parse_args()

# parse the URL
url_components = urlparse.urlparse(args.url)
if url_components.scheme == 'http':
    conn_factory = httplib.HTTPConnection
elif url_components.scheme == 'https':
    conn_factory = httplib.HTTPSConnection
else:
    print('Invalid scheme "%s". Should be http or https.' % url_components.scheme)
    sys.exit(1)

for i in range(args.iterations):
    if args.iterations > 1:
        print "******* Iteration: %d/%d ********" % (i + 1, args.iterations)

    # Create a Name identifying the target service
    service_name = gssapi.Name('HTTP@%s' % url_components.hostname,
                               name_type=gssapi.NameType.hostbased_service)

    # Create an InitContext targeting the service name
    ctx = gssapi.SecurityContext(name=service_name, usage='initiate',
        mech=gssapi.OID.from_int_seq((1, 3, 6, 1, 5, 5, 2)))

    # Create the connection
    conn = conn_factory(url_components.netloc)

    # Make the first request (which is different to the rest of them)
    try:
        conn.request("GET", url_components.path)
    except socket.error as e:
        print('Error connecting to %s: %s' % (args.url, e))
        sys.exit(1)

    # Get the response
    response = conn.getresponse()
    response.read()
    if 'Negotiate' not in response.getheader("www-authenticate"):
        print('The server does not support Negotiate authentication.')
        sys.exit(1)


    # Loop sending tokens to and from the server until the context is established
    in_token = None
    try:
        while not ctx.complete:
            out_token = ctx.step(in_token)
            if out_token:
                out_token_b64 = base64.b64encode(out_token)
                conn.request("GET", url_components.path,
                    headers={"Authorization": "Negotiate %s" % out_token_b64})

                response = conn.getresponse()
                data = response.read()
                in_token_b64 = response.getheader("www-authenticate")[10:]
                in_token = base64.b64decode(in_token_b64)

                if args.verbose:
                    print "**Token out**: %s" % out_token_b64
                    print "**Token in**: %s" % in_token_b64

            # if delay
            if args.delay:
                time.sleep(args.delay)

        # Upon success, print the received DATA
        print data
    except gssapi.exceptions.GSSError as e:
        print 'GSS error found: %s' % e
        sys.exit(1)
        
    # if delay, wait for the next iteration
    if args.wait:
        time.sleep(args.wait)
