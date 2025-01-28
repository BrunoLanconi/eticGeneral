# [Docker Compose](https://docs.docker.com/compose/reference/)

Docker Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services. Then, with a single command, you create and start all the services from your configuration.

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
```

- `services`: A list of services to run in the application.
- `web`: The name of the service.
- `build`: The path to the directory containing the Dockerfile.
- `ports`: The ports to expose on the host machine.
- `volumes`: The volumes to mount on the host machine.

`docker-compose.yaml` files abstract the `docker run` command, making it easier to manage multi-container applications.

---

## [Running a Compose Application](https://docs.docker.com/reference/cli/docker/compose/up/)

To run a Compose application, you can use the `docker compose up` command. This command reads the `docker-compose.yaml` file in the current directory and starts the services defined in it, building images if necessary and attaching to the containers' output.

**Note**: Sometimes you may see `docker-compose` instead of `docker compose`. This is because Docker Compose was originally a separate project before being integrated into Docker.

To stop the application, you can use the `docker compose down` command. This command stops and removes the containers, networks, images, and volumes created by `docker compose up`.

---

## Useful Commands and Flags

Mostly of `docker compose <command>` commands are similar to `docker <command>` commands - with the addition of the `compose` keyword and the use of the service name instead of the container ID.

- `docker compose run <service-name> <command>`: Run a one-off command on a service.
- `docker compose down`: Stop and remove containers, networks, images, and volumes.
- `docker compose logs`: View output from containers.
- `docker compose ps`: List services.
- `docker compose exec <service-name> <command>`: Run a command in a running service.
- `docker compose build`: Build or rebuild services.
- `docker compose up --build --no-cache`: Build the images and run the services without using the cache.