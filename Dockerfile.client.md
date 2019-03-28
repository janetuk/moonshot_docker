This image provides a ready-to-use Moonshot-enabled client, including SSH and curl.

## Environment variables
You MAY provide the following variables:
* `DISPLAY`. If you want to use the host's display (see below), you need to pass the `DISPLAY` environment variable to the container.

## Volumes:
You MAY provide volumes mapping the following targets:
* `/tmp/.X11-unix/X0/`. You may map this file from the host's `/tmp/.X11-unix/X0/` to grant the container access to the host's display. It requires a Linux host and having granted permissions on the host (e.g. by running `xhost +local:` or similar). You need this if you want to use the Moonshot GTK UI or Firefox, for instance.