# Lab 07: Docker Compose

Let's create a `docker-compose.yaml` file to run our FastAPI application and PostgreSQL database together.

## Prerequisites

- Docker installed on your system
- A text editor of your choice

## Instructions

1. You may use the last lab folder. Your project should look like this:

```bash
.
├── app
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src
│       ├── app.py
│       ├── config.py
│       └── db.py
└── postgres
    └── Dockerfile
```

2. On the last lab we needed to run the following commands to run our multi-container application:

```bash
docker build -t app app
docker build -t postgres postgres
docker network create --driver bridge app-network
docker run -d --rm --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres
docker run -it --rm --name app --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_HOST=postgres -e POSTGRES_DB=postgres -v ${PWD}/app:/app -p 8000:8000 app poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000
```

And then we needed to stop the containers using:

```bash
docker stop app postgres
```

3. Now let's create a `docker-compose.yaml` file to abstract these commands:

```bash
touch docker-compose.yaml
```

4. Add the `app` service to the `docker-compose.yaml` file:

```yaml
services:
  app:
    build:
      context: ./app
      dockerfile: Dockerfile
    command: poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
      POSTGRES_HOST: postgres
    ports:
      - "8000:8000"
    volumes:
      - ./app:/app
    networks:
      - app-network
    depends_on:
      - postgres
```

This configuration will build the `app` image using the `Dockerfile` in the `app` directory, set the environment variables, expose the port `8000`, mount the `app` directory to the container, and connect the container to the `app-network`. It abstracts the command to run the FastAPI application below:

```bash
docker run -it --rm --name app --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_HOST=postgres -e POSTGRES_DB=postgres -v ${PWD}/app:/app -p 8000:8000 app poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000
```

5. The `app` service depends on `postgres`, so let's add the `postgres` service to the `docker-compose.yaml` file:

```yaml
services:
  ...
  postgres:
    build:
      context: ./postgres
      dockerfile: Dockerfile
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: postgres
    ports:
      - "5432:5432"
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - app-network
```

This configuration will build the `postgres` image using the `Dockerfile` in the `postgres` directory, set the environment variables, expose the port `5432`, mount the `postgres-data` volume to the container, and connect the container to the `app-network`. It abstracts the command to run the PostgreSQL database below:

```bash
docker run -d --rm --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres
```

6. We also need to have both services connected to the same network, so let's add the `app-network` to the `docker-compose.yaml` file:

```yaml
...
networks:
  app-network:
    driver: bridge
```

7. Let's run the `docker-compose` command to build and start the services:

```bash
docker-compose up
```

### Optional Challenge

- Validate if `postgres` service data is being persisted deleting the `postgres` container and running `docker-compose up` again.
- Create the ways to persist the `postgres` data using volumes.
