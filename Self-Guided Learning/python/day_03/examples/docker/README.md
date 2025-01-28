# [Docker](https://www.docker.com/)

Docker is a platform for developers and sysadmins to develop, deploy, and run applications with containers. The use of Linux containers to deploy applications is called containerization. Containers are not new, but their use for easily deploying applications is.

##  Directory Structure

```bash
docker
├── Dockerfile
├── Makefile
└── README.md
```

## [Dockerfile](https://docs.docker.com/reference/dockerfile/) and [commands](https://docs.docker.com/reference/cli/docker/)

This file is used to build the Docker image.

```shell
docker build -t my-python-app .
```

- `build`: A subcommand to build a Docker image from a Dockerfile.
- `-t`: A flag to add a tag to the image.
- `.`: An argument to specify the path to the build context.

After building the image, you can run the container with the following command:

```shell
docker run -it --rm -v $(pwd):/app -p 8000:8000 my-python-app
```

- `run`: A subcommand to run a command in a new container.
- `-it`: A flag to allocate a pseudo-TTY connected to the container’s stdin.
- `--rm`: A flag to remove the container when it exits.
- `-v`: A flag to mount a volume.
- `$(pwd):/app`: An argument to specify the volume to mount. In this case, the current directory is mounted to the `/app` directory in the container.
- `-p`: A flag to publish a container’s port to the host.
- `8000:8000`: An argument to specify the port mapping. In this case, the container’s port 8000 is mapped to the host’s port 8000.
- `my-python-app`: An argument to specify the image tag to run.

## [Makefile](https://www.gnu.org/software/make/manual/make.html#Introduction)

In this folder we have an optional Makefile with the commands above.

```shell
bash                           Run a bash shell in the Docker container
build                          Build the Docker image
help                           Show help
run                            Run the Docker container
```

You can use the Makefile to run the commands:

```shell
make bash
```

The command above will build the Docker image and run a bash shell in the container, respectively.