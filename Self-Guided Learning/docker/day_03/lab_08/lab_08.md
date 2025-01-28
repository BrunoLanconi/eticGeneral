# Lab 08: Pruning

Let's nuke all the resources created by Docker.

## Prerequisites

- Docker installed on your system

## Instructions

**Note**: Before running the following commands, make sure you don't have any important data in your containers. This will remove all containers, networks, volumes, and images. If you want to preserve things, don't run these commands.

1. Remove all stopped containers:

```bash
docker container prune
```

2. Remove all networks not used by at least one container:

```bash
docker network prune
```

3. Remove all volumes not used by at least one container:

```bash
docker volume prune
```

4. Remove all images not used by at least one container:

```bash
docker image prune
```

5. Remove all unused data, including images, containers, volumes, and networks:

```bash
docker system prune
```

6. Use the `-a` flag to remove all unused data, including stopped containers, networks not used by at least one container, all images without at least one container associated to them, and all volumes not used by at least one container:

```bash
docker system prune -a --volumes
```

Now you have a clean Docker environment. You can start fresh with your containers and images.
