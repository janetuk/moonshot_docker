This image provides a ready-to-use Moonshot-enabled HTTP server. It is configured through a set of environment variables and volumes described below:

## Environment variables:
* `RPP`. The IP address or hostname of the RPP.

## Volumes:
You MUST provide volumes mapping the following targets:
* `/etc/ca.pem`. The CA certificate used for establishing the RADSEC connection to the RPP.
* `/etc/client.pem`. The client certificate used for establishing the RADSEC connection to the RPP.
* `/etc/client.key`. The private key for the client certificate.

You MAY provide volumes mapping the following targets:
* `/var/www/html/`. The site to be served. Anything under the `protected` folder will be protected with Moonshot. By default, there is a simple hello page.

You MAY also customise any aspect of the Apache server by creating volumes targeting its configuration files:
* `/etc/apache2`. Debian-style Apache configuration folder.
