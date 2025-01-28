# Binding

In Docker, you may bind ports, volumes, and networks to containers. This allows you to expose services, share files, and connect containers to each other.

---

## [Binding Ports](https://docs.docker.com/reference/cli/docker/container/run/)

To bind a port to a container, you can use the `-p` or `--publish` flag. This flag takes two arguments: the port on the host machine and the port on the container.

### Example
```bash
docker run -p 80:80 <image_name>
```

- `-p 80:80`: Bind port 80 on the host machine to port 80 on the container.

---

## [Binding Volumes](https://docs.docker.com/storage/bind-mounts/)

To bind a volume to a container, you can use the `-v` or `--volume` flag. This flag takes two arguments: the path on the host machine and the path on the container.

### Example
```bash
docker run -v /path/in/host:/path/in/container <image_name>
```

- `-v /path/in/host:/path/in/container`: Bind the directory `/path/in/host` on the host machine to the directory `/path/in/container` on the container.

---

## [Binding Networks](https://docs.docker.com/network/)

To bind a network to a container, you can use the `--network` flag. This flag takes the name of the network as an argument.

### Example
```bash
docker run --network my_network <image_name>
```

- `--network my_network`: Bind the network `my_network` to the container.

You can also use the `--network-alias` flag to assign an alias to the container on the network.
