This image provides a ready-to-use Trust Router server. It is configured through a set of environment variables and volumes described below:

## Environment variables:
* `APC_HOSTNAME`. Hostname of the APC server.

## Volumes:
You MUST provide volumes mapping the following targets:
* `/etc/ca.pem`. The CA certificate used for establishing the RADSEC connection to the APC.
* `/etc/client.pem`. The client certificate used for establishing the RADSEC connection to the APC.
* `/etc/client.key`. The private key for the client certificate.
* `/credential.xml`. The Moonshot credential file for this server.
* `/etc/trust_router/conf.d/default/`. A folder containing the trust router configuration files.
