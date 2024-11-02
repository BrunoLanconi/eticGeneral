# Project A

## Overview

This project utilizes Docker and Poetry to manage a PostgreSQL database and a Python development environment. Below are the available make commands to help you manage and interact with the project.

## Docker Compose Configuration

The project includes a `docker-compose.yml` file to manage the services required for development. Below is an overview of the services defined in the file:

### Services

- **poetry**: This service builds the development environment using a Dockerfile located at `ops/poetry.Dockerfile`. It sets up environment variables for connecting to the PostgreSQL database.
- **database**: This service uses the official PostgreSQL image and sets up the database with the specified environment variables. It also mounts volumes for persistent data storage and initialization scripts.
- **adminer**: This service uses the Adminer image to provide a web-based interface for managing the PostgreSQL database. It maps port 5433 on the host to port 8080 in the container.

### Volumes

- **data**: This volume is used to persist the PostgreSQL data.

### Networks

- **poetry-network**: This custom bridge network is used to facilitate communication between the services.

To start the services, run:
```sh
docker-compose up -d
```

To stop the services, run:
```sh
docker-compose down
```

## Makefile Commands

### General Commands

- **help**: Show help
  ```sh
  make help
  ```

- **clean**: Stop and remove containers
  ```sh
  make clean
  ```

### Development Commands

- **dev-build**: Build the dev container
  ```sh
  make dev-build
  ```

- **dev-bash**: Run bash in the dev container
  ```sh
  make dev-bash
  ```

- **dev-init**: Initialize a new poetry project
  ```sh
  make dev-init
  ```

- **dev-add**: Add a package to the poetry project
  ```sh
  make dev-add package=<package_name>
  ```

- **dev-main**: Run the main.py file
  ```sh
  make dev-main
  ```

- **dev-up**: Start the dev container
  ```sh
  make dev-up
  ```

### Linting

- **lint**: Run the linter
  ```sh
  make lint
  ```

## Usage

To get started, you can build the development container using:
```sh
make dev-build
```

Then, you can start the container with:
```sh
make dev-up
```

For more commands and their descriptions, you can always refer to the help command:
```sh
make help
```

## License

This project is licensed under the MIT License.