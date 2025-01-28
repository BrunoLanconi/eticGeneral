## Commands Cheat Sheet

Below is a non-exhaustive list of commands that you may find useful when working with Docker.

### Docker Commands

- `/etc/init.d/docker start`: Starts the Docker service.
- `docker build -f <dockerfile_path> -t <username>/<image_name>:<tag>`: Builds an image from a Dockerfile with a specific tag.
- `docker build -f <dockerfile_path> -t <username>/<image_name>`: Builds an image from a Dockerfile with a specific tag.
- `docker build -f <dockerfile_path>`: Builds an image from a Dockerfile.
- `docker container logs --tail 100 <container_name>`: Shows the last 100 lines of logs for a container.
- `docker container prune`: Removes all stopped containers.
- `docker exec -it <container_name> "pwd"`: Executes a command in a running container.
- `docker exec -it container "/bin/sh"`: Executes a shell in a running container.
- `docker inspect <container_id>`: Shows detailed information on a container.
- `docker login`: Logs in to a Docker registry.
- `docker network create --driver bridge <network_name>`: Creates a new bridge network.
- `docker network ls`: Lists all networks.
- `docker ps -a`: Lists all containers, including stopped ones.
- `docker ps`: Lists all running containers.
- `docker pull <username>/<image_name>`: Pulls an image from a Docker registry.
- `docker push <username>/<image_name>`: Pushes an image to a Docker registry.
- `docker rm <container_id>`: Removes a container.
- `docker rmi $(docker images -a -q) -f`: Removes all images forcefully.
- `docker rmi $(docker images -a -q)`: Removes all images.
- `docker rmi <image_name>`: Removes an image.
- `docker run -d -P --name <container_name> <image_name>`: Creates and starts a container from an image in detached mode with a specific name.
- `docker run -d -p 12345:80 <image_name>`: Creates and starts a container from an image in detached mode and maps port 12345 on the host to port 80 on the container.
- `docker run -it --name <container_name> --network <network_name> <image_name> /bin/bash`: Creates and starts a container from an image in interactive mode with a specific name and on a specific network.
- `docker run -it <image_name>`: Creates and starts a container from an image in interactive mode.
- `docker run -v "<volume_path>" <image_name>`: Creates and starts a container from an image and mounts a volume.
- `docker run <image_name>`: Creates and starts a container from an image.
- `docker start -a -i <container_id>`: Starts a stopped container in interactive mode.
- `docker start <container_id>`: Starts a stopped container.
- `docker stop <container_id>`: Stops a running container.
- `docker version`: Shows the Docker version information.
- `docker compose build`: Builds the services defined in a Compose file.
- `docker compose down`: Stops and removes the services defined in a Compose file.
- `docker compose ps`: Lists the services defined in a Compose file.
- `docker compose up --build`: Creates and starts the services defined in a Compose file and rebuilds the images.
- `docker compose up`: Creates and starts the services defined in a Compose file.
- `hostname -i`: Shows the IP address of the container.