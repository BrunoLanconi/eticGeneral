## [Commands](https://docs.docker.com/reference/)

Docker has a lot of commands that you can use to interact with the Docker daemon. Here are some of the most common commands that you'll use:

- `docker build`: Build an image from a Dockerfile.
- `docker exec`: Run a command in a running container.
- `docker images`: List images on your system.
- `docker ps`: List running containers.
- `docker pull`: Pull an image from a registry.
- `docker push`: Push an image to a registry.
- `docker rm`: Remove a container.
- `docker run`: Run a command in a new container.
- `docker start`: Start a stopped container.
- `docker stop`: Stop a running container.

---

## [Build](https://docs.docker.com/reference/cli/docker/buildx/build/)

The `docker build` command is used to build an image from a Dockerfile.

### Example
```bash
docker build -t my-image .
```

- `-t my-image`: Tag the image with the name `my-image`.
- `.`: Use the current directory as the build context.

---

## [Exec](https://docs.docker.com/reference/cli/docker/container/exec/)

The `docker exec` command is used to run a command in a running container.

### Example
```bash
docker exec my-container ls -l
```

- `my-container`: The name or ID of the container.
- `ls -l`: The command to run in the container.

---

## [Image](https://docs.docker.com/reference/cli/docker/image/)

The `docker image` command is used to manage images on your system.

### Example
```bash
docker image ls
```

- `ls`: List all images on your system.

---

## [Run](https://docs.docker.com/reference/cli/docker/container/run/)

The `docker run` command is used to run a command in a new container.

### Example
```bash
docker run -d -p 8080:80 my-image
```

- `-d`: Run the container in detached mode.
- `-p 8080:80`: Map port `8080` on the host to port `80` in the container.
- `my-image`: The name or ID of the image to run.

### Example
```bash
docker run -it --rm my-nginx /bin/sh
```

- `-it`: Run the container in interactive mode with a TTY.
- `--rm`: Remove the container when it exits.
- `my-nginx`: The name or ID of the image to run.
- `/bin/sh`: The command to run in the container.

"Bashing" into a container is a common practice to debug or inspect the container. In order to do this, you need to have a shell available in the container and you must pass the `-it` flags to the `docker run` command, which will keep the STDIN open and allocate a pseudo-TTY.

---

## [Rm](https://docs.docker.com/reference/cli/docker/container/rm/)

The `docker rm` command is used to remove a container.

### Example
```bash
docker rm my-container
```

- `my-container`: The name or ID of the container.
