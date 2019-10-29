# Moonshot Docker images
This repository provides the required Dockerfiles to set up a fully docker-based Moonshot infrastructure.

# How to use it
There are 2 different ways in which you can use these images:

## Build the images individually and use them directly
The most advanced way of using these images is to build them individually and run them to create your own Moonshot infrastructure.
In that case, you must provide all the configuration they require, and make sure everything is set up correctly.

You can build any of the Dockerfiles independently, using a command similar to the following:
```
docker build -f Dockerfile.tr -t moonshot-trust-router .
```
It would be similar for the rest of components, changing Dockerfile and the tagged name.
You can find pre-built images in our Docker Hub (https://hub.docker.com/u/jiscmoonshot)

Then, you can run the images. Instructions on how to use each resulting images can be found in this repository:
* [APC](Dockerfile.apc.md)
* [Trust Router](Dockerfile.tr.md)
* [IDP](Dockerfile.idp.md)
* [HTTP server](Dockerfile.httpserver.md)
* [SSH server](Dockerfile.sshserver.md)
* [Client](Dockerfile.client.md)

For example, to run a Moonshot IDP connected to the Moonshot Playpen infrastructure, you would execute something similar to the following:
```
docker run -ti -e IDP_REALM=my.test.realm -e TR_GSSNAME=trustrouter@apc.test.assent -e TR_HOSTNAME=tr.moonshot-playpen.ti.ja.net -e APC_REALM=apc.test.assent -v $PATH_CA_PEM:/etc/ca.pem -v $PATH_CLIENT_PEM:/etc/client.pem -v $PATH_CLIENT_KEY:/etc/client.key -v $PATH_CREDENTIAL_XML:/credential.xml -v $PATH_SERVER_PEM:/etc/freeradius/certs/server.pem -v $PATH_SERVER_KEY:/etc/freeradius/certs/server.key -v $PATH_USERS_FILE:/etc/freeradius/mods-config/files/idp_users.txt moonshot-idp
```

## Use the shipped Docker-compose based demo
A second way of using these images is by using the shipped Docker-compose file.
It set ups a simple Moonshot test network with the following components:
* One APC
* A Trust Router server
* Two IDPs. Both have a user called `alice` whose password is `alicepwd`.
* An SSH server connected to IDP1
* An HTTP server connected to IDP1
* A Client with credentials for alice at both IDPs

### Building and running the demo
To build and run the infrastructure, just use:
```
docker-compose up -d --force-recreate --build
```

### Executing commands
You can execute commands on any of the different components by using `docker-compose exec`.

For instance, you can execute bash on the client to get an interactive session by using:
```
docker-compose exec client bash
```

If your host system is running an X session, you can share it with the client container by passing the DISPLAY variable.
If that's the case, the client container will use the Moonshot GTK UI. Otherwise, the TEXT UI is used.
The only requirement is to make sure you allow docker to use the display. This can be safely done by issuing the:
```
xhost +local:
```

After that, you can execute graphical applications within the client container.
```
docker-compose exec -e DISPLAY client moonshot
```

### Checking logs
Most of the components are run in foreground mode. That means that their log output is written to the standard output,
and can be checked with the `docker-compose logs` functionality.

For instance, you can attach to IDP1's log output by executing:
```
docker-compose logs -f idp1
```

### Test script
Finally, we provide a test script that makes use of `docker-compose exec` (as described above)
to import the user credentials on the client and then perform one authentication to the SSH server and one to the HTTP server.


