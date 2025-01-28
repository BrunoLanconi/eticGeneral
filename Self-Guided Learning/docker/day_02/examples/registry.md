# [Pushing](https://docs.docker.com/reference/cli/docker/image/push/) and [Pulling](https://docs.docker.com/reference/cli/docker/image/pull/) Images from a [Registry](https://hub.docker.com/search?q=)

We can push and pull images from a registry. A registry is a storage and content delivery system, holding named Docker images, available in different tagged versions. The most common registry is Docker Hub.

---

## Pushing an Image to a Registry

To push an image to a registry, you must first tag it with the registry name.

- On build:

### Example
```bash
docker build -t <registry-name>/<image-name>:<tag> .
```

- After build:

### Example
```bash
docker build -t <image-name>:<tag> .
docker tag <image-name>:<tag> <registry-name>/<image-name>:<tag>
```

Then, you can push the image to the registry:

### Example
```bash
docker push <registry-name>/<image-name>:<tag>
```

Some registries require [authentication](https://docs.docker.com/reference/cli/docker/login/). You can authenticate with the registry using the `docker login` command.

### Example
```bash
docker login <registry-name>
```

---

## Pulling an Image from a Registry

To pull an image from a registry, you can use the `docker pull` command:

### Example
```bash
docker pull <registry-name>/<image-name>:<tag>
```

If you don't specify a tag, Docker will pull the `latest` tag by default.

### Example
```bash
docker pull <registry-name>/<image-name>
```

You can also pull an image from a private registry by authenticating with the registry using the `docker login` command.

### Example
```bash
docker login <registry-name>
```

---

## Searching for Images on a Registry

You can search for images on a registry using the `docker search` command:

### Example
```bash
docker search <search-term>
```
