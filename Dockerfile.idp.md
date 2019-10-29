This image provides a ready-to-use Moonshot IDP. It is configured through a set of environment variables and volumes described below:

## Environment variables:
* `IDP_REALM`. The realm for this IDP.
* `TR_GSSNAME`. The GSS name of the Trust Router server.
* `TR_HOSTNAME`. The hostname of the Trust Router server.
* `APC_REALM`. The APC realm.

## Volumes:
You MUST provide volumes mapping the following targets:
* `/etc/ca.pem`. The CA certificate used for establishing the RADSEC connection to itself.
* `/etc/client.pem`. The client certificate used for establishing the RADSEC connection to itself.
* `/etc/client.key`. The private key for the client certificate.
* `/credential.xml`. The Moonshot credential file for this server.

You MAY provide volumes mapping the following targets:
* `/etc/freeradius/certs/server.pem`. The server certificate used for this server. If not provided, a stock *UNSECURE* one is used.
* `/etc/freeradius/certs/server.key`. The private key for the server certificate. If not provided, a stock *UNSECURE* one is used.
* `/etc/freeradius/mods-config/files/idp_users.txt`. List of the credentials handled by this IDP (using FreeRadius users syntax). By default it contains `alice    Cleartext-Password := "alicepwd"`.
* `/etc/freeradius/policy.d/moonshot_saml`.  A FreeRadius policy file that allows you to customise how SAML Assertions are generated. By default, it just includes a hardcoded Assertion where the `entitlement` attribute value is always set to `moonshot`.
