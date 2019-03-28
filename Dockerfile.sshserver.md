This image provides a ready-to-use Moonshot-enabled SSH server. It is configured though a set of environment variables and volumes described below:

## Environment variables:
* `RPP`. The IP address or hostname of the RPP.
* `USERS`. A list of account names to be created, delimited by `:`.

## Volumes:
You MUST provide volumes mapping the following targets:
* `/etc/ca.pem`. The CA certificate used for establishing the RADSEC connection to the RPP.
* `/etc/client.pem`. The client certificate used for establishing the RADSEC connection to the RPP.
* `/etc/client.key`. The private key for the client certificate.

You MAY provide volumes mapping the following targets:
* `/etc/shibboleth/attribute-map.xml`. You might want to customise this file in order to use a different source for the `local-login-user` attribute. By default, it uses the SAML`entitlement` attribute.
