## Images

Docker images are read-only templates that define an application's environment. They contain everything needed to run an application, including libraries, dependencies, and configuration files. Images are created from a [Dockerfile](https://docs.docker.com/reference/dockerfile/) and stored in a registry, such as [Docker Hub](https://hub.docker.com/search?q=). Images can be shared and reused to [create containers](https://docs.docker.com/reference/cli/docker/container/run/).

When [building](https://docs.docker.com/reference/cli/docker/buildx/build/) an image locally, Docker uses a cache to speed up the process. If a layer has not changed, Docker will use the cached layer instead of rebuilding it. This can save time when building images with many layers.

Locally builded images are stored in the local Docker registry. You can view the images on your system using the `docker images` command.

---

## [Dockerfile](https://docs.docker.com/reference/dockerfile/)

The Dockerfile is a text file that defines how to build an image. Each line defines a layer in the image, and the layers are built in order. Usually, the Dockerfile starts with a `FROM` instruction that specifies the base image to use. The Dockerfile can include other instructions, such as `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `ENV` and `CMD`, to configure the image.

There are lots of instructions that can be used in a Dockerfile.

### Example
```Dockerfile
# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

- `FROM`: Specifies the base image to use.
- `WORKDIR`: Sets the working directory in the container.
- `COPY`: Copies files from the host to the container.
- `RUN`: Runs a command in the container.
- `EXPOSE`: Exposes a port in the container.
- `ENV`: Sets an environment variable.
- `CMD`: Specifies the command to run when the container starts.

---

## [Entrypoint](https://docs.docker.com/reference/builder/#entrypoint)

The `ENTRYPOINT` instruction in a Dockerfile specifies the command to run when the container starts. The `ENTRYPOINT` instruction can be complemented at runtime by specifying a command when running the container.

### Example
```Dockerfile
FROM python:3.9-slim

...

# Run app.py when the container launches
COPY .entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
```

### Example
```bash
#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo "bash - Runs bash"
    echo "run - Runs NGINX"
}

case ${1} in
bash)
    exec bash
    ;;
run)
    exec nginx -g 'daemon off;'
    ;;
*)
    print_help
    ;;
esac
```

With this setup, you can run the container with different commands, such as `bash` or `run`.

```bash
docker run -it my-nginx bash
docker run -d my-nginx run
```

---

## [Layers](https://docs.docker.com/build/guide/layers/)

An image layer is a read-only filesystem that represents a single instruction in a Dockerfile. Each instruction in a Dockerfile creates a new layer in the image. Layers are stacked on top of each other to create the final image. When a container is created from an image, a read-write layer is added on top of the image layers to store any changes made to the container.

---

## [Registry](https://docs.docker.com/registry/)

A Docker registry is a storage and distribution system for named Docker images. It can be public or private and can be hosted on-premises or in the cloud. [Docker Hub](https://hub.docker.com/search?q=) is a public registry that hosts thousands of images that can be used to create containers.
