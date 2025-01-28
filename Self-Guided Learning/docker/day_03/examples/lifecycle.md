# Container Lifecycle

A container lifecycle has three main states:

1. **Created**: The container is created but not started.
2. **Running**: The container is running and executing commands.
3. **Stopped**: The container has stopped running.

The container may also be **Restarted** if it is configured to do so.

```yaml
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    restart: always
```

The container [restart policy](https://docs.docker.com/reference/cli/docker/container/run/#restart) can be set to `no`, `always`, `on-failure`, or `unless-stopped`.

```bash
docker run --restart always my-app
```

---

## [Starting a Container](https://docs.docker.com/reference/cli/docker/container/start/)

To start a container, use the command alias `docker start` command followed by the container ID or name. This command is an alias for `docker container start`.

```bash
docker start <container_id>
```

---

## [Stopping a Container](https://docs.docker.com/reference/cli/docker/container/stop/)

To stop a running container, use the command alias `docker stop` command followed by the container ID or name. This command is an alias for `docker container stop`.

```bash
docker stop <container_id>
```

---

## [Deleting a Container](https://docs.docker.com/reference/cli/docker/container/rm/)

To delete a container, use the command alias `docker rm` command followed by the container ID or name. This command is an alias for `docker container rm`.

```bash
docker rm <container_id>
```
