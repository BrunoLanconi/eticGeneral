# Lab 03: Running

Now that you have your own image and it is built, let's perform some running commands on different states of its lifecycle. In this lab, you'll run a container, overwrite the container default command and execute commands against a running container.

## Prerequisites

- Docker installed on your system
- A text editor of your choice

## Instructions

1. List the running containers within your system:

```bash
docker ps
```

2. If no containers are listed, you may run a detached container:

```bash
docker run -d simple-web-server
```

**Hint**: Use the image built from previous lab Dockerfile.

3. List the running containers again:

```bash
docker ps
```

You should see the container running with the image you built. Something like this:

```bash
CONTAINER ID   IMAGE              COMMAND                  CREATED         STATUS         PORTS     NAMES
<container_id> simple-web-server  "nginx -g 'daemon of…"   5 seconds ago   Up 4 seconds   80/tcp    <container_name>
```

4. Execute a command against the running container:

```bash
docker exec <container_id> cat /usr/share/nginx/html/index.html
```

This command will output the content of the `index.html` file that you copied into the container.

5. Stop the running container:

```bash
docker stop <container_id>
```

6. List the running containers again:

```bash
docker ps
```

You should see no containers running.

7. Run a container with a different command:

```bash
docker run -it simple-web-server sh
```

This command will run the container in interactive mode with a shell prompt.

### Optional Challenge

- Create a `entrypoint.sh` script that outputs a message when the container starts. Update the Dockerfile to use this script as the entrypoint. Build the image and run a container to see the message.

### Example
```Dockerfile
# Dockerfile
...
COPY .entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
```
