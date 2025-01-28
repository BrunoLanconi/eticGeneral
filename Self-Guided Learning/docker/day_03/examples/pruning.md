# [Pruning](https://docs.docker.com/engine/manage-resources/pruning/)

Pruning is the process of removing unused images and volumes from your system. This is useful to free up disk space and to keep your system clean.

```bash
docker <command> prune
```

- `command`: The command to prune the resources. It can be `image`, `container`, `volume`, `network`, or `system`.

---

## [System Prune](https://docs.docker.com/reference/cli/docker/system/prune/)

Use the `docker system prune` command to remove all unused data, including images, containers, volumes, and networks.

### Example
```bash
docker system prune
```

This will remove all stopped containers, all networks not used by at least one container, all dangling images, and all build cache.

---

## Nuke Everything

Use the `-a` flag to remove all unused data, including stopped containers, networks not used by at least one container, all images without at least one container associated to them, and all volumes not used by at least one container.

### Example
```bash
docker system prune -a
```
