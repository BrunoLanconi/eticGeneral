# [Arguments](https://docs.docker.com/build/guide/build-args/) and [Environment Variables](https://docs.docker.com/compose/environment-variables/set-environment-variables/)

Arguments and environment variables are two ways to pass configuration values to a Docker container. Arguments are used during the build process, while environment variables are used during the runtime of the container.

---

## Passing Arguments

Arguments are used to pass configuration values to the Dockerfile during the build process. They are defined using the `ARG` instruction in the Dockerfile.

### Example
```dockerfile
# Dockerfile

ARG APP_VERSION=latest
```

To build the image with the argument `APP_VERSION` set to `1.0`, you can use the `--build-arg` flag:

### Example
```bash
docker build --build-arg APP_VERSION=1.0 -t my-app .
```

The argument `APP_VERSION` can be used in the Dockerfile to set the version of the application:

### Example
```dockerfile
# Dockerfile

ARG APP_VERSION=latest

RUN echo "Building version $APP_VERSION"
```

---

## Setting Environment Variables

Environment variables are used to pass configuration values to the container during runtime. They are defined using the `ENV` instruction in the Dockerfile.

### Example
```dockerfile
# Dockerfile

ENV APP_ENV=production
```

To run the container with the environment variable `APP_ENV` set to `development`, you can use the `-e` flag:

### Example
```bash
docker run -e APP_ENV=development my-app
```

---

## Using Arguments and Environment Variables on Docker Compose

You can use arguments and environment variables in Docker Compose to pass configuration values to the services defined in the `docker-compose.yaml` file.

### Example
```yaml
# docker-compose.yaml

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        APP_VERSION: 1.0
    environment:
      APP_ENV: development
```

In this example, the `app` service is built with the argument `APP_VERSION` set to `1.0` and the environment variable `APP_ENV` set to `development`.

---

## `.env` File

You can also use a `.env` file to define environment variables that will be automatically loaded by Docker Compose.

### Example
```env
# .env

APP_ENV=development
```

The `.env` file can be used in the `docker-compose.yaml` file as follows:

### Example
```yaml
# docker-compose.yaml

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    env_file:
      - .env
```

In this example, the `APP_ENV` environment variable will be set to `development` when running the `app` service.
