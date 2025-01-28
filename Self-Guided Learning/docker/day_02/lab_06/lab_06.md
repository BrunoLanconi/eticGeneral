# Lab 06: Pushing and Pulling

Let's push the Docker image we created in the last lab to Docker Hub and pull it from there.

## Prerequisites

- Docker installed on your system

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
2. Create a Docker Hub account at [hub.docker.com](https://hub.docker.com/).
3. Login to Docker Hub:

```bash
docker login
```

4. Build the Docker image:

```bash
docker build -t app:latest app
```

3. Tag the image with your Docker Hub username:

```bash
docker tag app:latest <username>/app:latest
```

4. Push the image to Docker Hub:

```bash
docker push <username>/app:latest
```

5. Pull the images from Docker Hub:

```bash
docker pull <username>/app:latest
```

6. Now that you have the image on Docker Hub, you can use it as a base image for other projects.

```Dockerfile
# Use the image from Docker Hub as the base image
FROM <username>/app:latest
```

### Optional Challenge

- Edit the new Dockerfile to use the image from Docker Hub as the base image.
- Add a `CMD` instruction to run the application.
- Add the necessary environment variables to the Dockerfile.

Then the run command should look like this:

```bash
docker run -it --rm --name app --network app-network -v ${PWD}/app:/app -p 8000:8000 app
```
