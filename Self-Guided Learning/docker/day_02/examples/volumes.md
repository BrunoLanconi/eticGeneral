# [Volumes and Mounts](https://docs.docker.com/engine/storage/)

(...) Volumes are stored in a part of the host filesystem which is managed by Docker (...). Non-Docker processes should not modify this part of the filesystem. Volumes are the best way to persist data in Docker.

Bind mounts may be stored anywhere on the host system. They may even be important system files or directories. Non-Docker processes on the Docker host or a Docker container can modify them at any time.

`tmpfs` mounts are stored in the host system's memory only, and are never written to the host system's filesystem.

Bind mounts and volumes can both be mounted into containers using the `-v` or `--volume` flag, but the syntax for each is slightly different. For `tmpfs` mounts, you can use the `--tmpfs` flag. We recommend using the `--mount` flag for both containers and services, for bind mounts, volumes, or `tmpfs` mounts, as the syntax is more clear.

### Example
```bash
docker run -v /path/in/host:/path/in/container:ro <image_name>
```

- `-v` or `--volume`: Create a bind mount or volume. Consists in three fields, separated by colon characters (`:`). 

The fields must be in the following order:

- `source`: The first field is the path to the file or directory on the host machine.
- `destination`: The second field is the path where the file or directory is mounted in the container.
- `options`: The third field is optional, and is a comma-separated list of options, such as `ro` (read-only) or `rw` (read-write).

### Example
```bash	
docker run --mount type=bind,source=/path/in/host,target=/path/in/container,readonly <image_name>
```

- `--mount`: Create a bind mount, volume, or `tmpfs` mount. Consists in a comma-separated list of key-value pairs.

The keys are as follows:

- `type`: The type of mount. Can be `bind`, `volume`, or `tmpfs`.
- `source`: The source of the mount. For a bind mount, this is the path to the file or directory on the host machine. For a volume, this is the name of the volume.
- `target`: The path where the file or directory is mounted in the container.

---

## [Anonymous and Named Volumes](https://docs.docker.com/engine/storage/volumes/)

Volumes can be either anonymous or named. Anonymous volumes are not given a specific name when they are first mounted into a container, so Docker gives them a random name. You can see the anonymous volumes in the output of `docker volume ls`. Named volumes have a specific name that you specify when you create the volume. You can see the named volumes in the output of `docker volume ls`. Prefer to use volumes instead of bind mounts for persistent data.

### Example
```bash
docker run -v /path/in/container <image_name>
```

- `-v /path/in/container`: Create an anonymous volume in the container at `/path/in/container`.

### Example
```bash
docker run -v volume_name:/path/in/container <image_name>
```

- `-v volume_name:/path/in/container`: Create a named volume named `volume_name` in the container at `/path/in/container`.

### Example
```bash
docker run -v /path/in/host:/path/in/container <image_name>
```

- `-v /path/in/host:/path/in/container`: Create a bind mount in the container at `/path/in/container` pointing to `/path/in/host` on the host machine.

You may also use the `--mount` flag to create named volumes:

### Example
```bash
docker run --mount type=volume,source=volume_name,target=/path/in/container <image_name>
```
