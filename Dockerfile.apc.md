This image provides a ready-to-use APC. It is configured thought a set of environment variables and volumes described below:

This image provides a ready-to-use Moonshot IDP. It is configured thought a set of environment variables and volumes described below:

## Environment variables:
* `APC_REALM`. The realm for this APC.
* `TR_GSSNAME`. The GSS name of the Trust Router server.

## Volumes:
You MUST provide volumes mapping the following targets:
* `/etc/ca.pem`. The CA certificate used for establishing the RADSEC connection to itself.
* `/etc/client.pem`. The client certificate used for establishing the RADSEC connection to itself.
* `/etc/client.key`. The private key for the client certificate.

You MAY provide volumes mapping the following targets:
* `/etc/freeradius/certs/server.pem`. The server certificate used for this server. If not provided, a stock *UNSECURE* one is used.
* `/etc/freeradius/certs/server.key`. The private key for the server certificate. If not provided, a stock *UNSECURE* one is used.
* `/etc/freeradius/mods-config/files/apc_users.txt`. List of the credentials for the IDP/RPP belonging to the APC (using FreeRadius users syntax). 
