# Moonshot Docker images
This repository provides the required Dockerfile to set up a fully docker-based Moonshot network.

# How to use it
There are 3 different ways in which you can use test this images:

## Build the images individually and use them directly
The most advanced way of using these images is to build them individually and run them to create your own Moonshot network.
In that case, you must provide all the configuration they require, and make sure everything is set up correctly.

You can build any of the Dockerfile files independently, using the following command:
```
docker build -f Dockerfile.tr -t moonshot-trust-router .
```
It would be similar for the rest of components.

Then, you can run the images. Instructions on how to use each resulting images can be found in this repository:
* [APC](Dockerfile.apc.md)
* [Trust Router](Dockerfile.tr.md)
* [IDP](Dockerfile.idp.md)
* [HTTP server](Dockerfile.httpserver.md)
* [SSH server](Dockerfile.sshserver.md)
* [Client](Dockerfile.client.md)

For example, to run a Moonshot IDP connected to the Moonshot Playpen infrastructure, you would execute something similar to the following:
```
docker run -ti -e IDP_REALM=my.test.realm -e TR_GSSNAME=trustrouter@apc.test.assent -e TR_HOSTNAME=tr.moonshot-playpen.ti.ja.net -e APC_REALM=apc.test.assent -v $PATH_CA_PEM:/etc/ca.pem -v $PATH_CLIENT_PEM:/etc/client.pem -v $PATH_CLIENT_KEY:/etc/client.key $PATH_CREDENTIAL_XML:/credential.xml -v $PATH_SERVER_PEM:/etc/freeradius/certs/server.pem -v $PATH_SERVER_KEY:/etc/freeradius/certs/server.key -v $PATH_USERS_FILE:/etc/freeradius/mods-config/files/idp_users.txt
```

## Docker compose
A second way of using these images is by using the shipped Docker compose file. It set ups a simple Moonshot test network with the following components:
* An APC
* A Trust Router server
* Two IDPs. Both have a user called `alice` whose password is `alicepwd`.
* An SSH server connected to IDP1
* An HTTP server connected to IDP1
* A Client with credentials for both IDPs

To build and run the infrastructure, just use:
```
docker-compose up -d --build
```

After the components are running, you can issue commands directly by using:
```
docker-compose exec client command-to-execute
```

Or just "log in" by executing a bash session:
```
docker-compose exec client bash
```

You can check the logs at any point by issuing:
```
docker-compose logs idp1
```

## Test script
The third way of using these imges is by using the shipped `test.sh` script. It starts the docker compose and issues a series of simple commands to:
1. Install the credentials into the Client
2. Connect to the SSH server
3. Connect to the HTTP server

If the host's display is available, it will use the GTK UI. If it is not, it will use the TXT UI.

You can check out the logs as described above.


