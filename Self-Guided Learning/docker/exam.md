# Exam

Below you will find a list of questions that you need to answer. The questions are grouped by day as they were presented in the course. 

- Day 01: Docker Intro
- Day 02: Docker Concepts
- Day 03: Docker Fundamentals

Each day has at least 02 questions of multiple choice, multiple selection or true or false. Each question has a weight that represents the importance of the question. The total sum of the weights is 100. The exam is open book, meaning you can use any resources you want to answer the questions. You can use the internet, your notes, the course materials, etc. You can also use the terminal, but try to use none or as little as possible in order to challenge yourself. The exam is individual, meaning you should not discuss the questions with your colleagues. You have 1 hour to complete the exam. Good luck!

---

## Day 01: Docker Intro

### Question 1 (weight: 5; total: 5)

About virtual machine and containers, select the correct statements:

[] Containers are lightweight and share the host OS kernel
[] VMs and containers abstracts physical hardware
[] VMs require guest OS
[] Containers are slower than VMs
[] Containers are more secure than VMs

### Question 2 (weight: 5; total: 10)

A Dockerfile is:

a) A file that contains the instructions to run a Docker container
b) A file that contains the instructions to build a Docker image
c) A file that contains the instructions to build a Docker container
d) A file that contains the instructions to run a Docker image

### Question 3 (weight: 5; total: 15)

A registry is:

a) A place where you can run your Docker containers
b) A place to register the bind mounts
c) A place where you can store your Docker containers
d) A place where you can store your Docker images

### Question 4 (weight: 5; total: 20)

A developer wants to `bash` into a running container. Which command should be used?

a) `docker run -it <container_id> bash`
b) `docker exec -it <container_id> bash`
c) `docker start -it <container_id> bash`
d) `docker attach -it <container_id> bash`

### Question 5 (weight: 5; total: 25)

In a Dockerfile, the developers found the following instructions: 

```Dockerfile
...
CMD ["python", "app.py"]
...
```

But he wants to override the command and run the container with the command `python app.py --debug`. Which command should be used?

a) `docker run -it <image_id> --entrypoint "python app.py" --debug`
b) `docker run -it <image_id> --entrypoint "python app.py --debug"`
c) `docker run -it <image_id> python app.py --debug`
d) `docker run -it <image_id> --entrypoint "python app.py" -- --debug`

### Question 6 (weight: 10; total: 35)

Given the following Dockerfile:

```Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
```

And the following `tree` output:

```bash
.
├── Dockerfile
├── app.py
└── requirements.txt
```

The developer complains that the container is not running the `app.py` file. What is the problem?

a) The `WORKDIR` should be `/app/` or the same name as the directory
b) The `CMD` instruction is wrong
c) The `app.py` file is not being copied to the container
d) The `requirements.txt` file is not being copied to the container

---

## Day 02: Docker Concepts

### Question 7 (weight: 5; total: 40)

About Docker volumes, select the correct statements:

[] Volumes are used to persist data between container restarts
[] Volumes are used to share data between containers
[] Volumes are used to share data between the host and the container
[] Volumes are used to share data between the host and the image
[] Volumes are used to share data between the image and the container

### Question 8 (weight: 5; total: 45)

The developer wants to push a Docker image to a registry with hostname `registry.example.com` and repository `myapp`. The image should be tagged as `latest`. Which command should be used?

a) `docker push registry.example.com/myapp/latest`
b) `docker tag <image_id> registry.example.com/myapp` and `docker push registry.example.com/myapp`
c) `docker tag <image_id> registry.example.com/myapp` and `docker push --latest registry.example.com/myapp`
d) `docker tag <image_id> registry.example.com/myapp`

### Question 9 (weight: 5; total: 50)

All application files are in `app/` directory. The developer wants to run the application in a container and make the application files available in the container. Which command should be used?

a) `docker bind-volume app/:/app <container_id>`
b) `docker build -v app/:/app .`
c) `docker run -v app/:/app <container_id>`
d) `docker run -v app/:/app <image_id>`

### Question 10 (weight: 5; total: 55)

The developer wants to run a container with the following requirements:

- The container should be named `myapp`
- The container should run in the background
- The container should be removed when it stops
- The container should expose port 80
- The container should have the environment variable `DEBUG` set to `true`

Which command should be used?

a) `docker run -d -remove --name myapp --port 80 -e DEBUG=true <image_id>`
b) `docker run -d --rm --name myapp -p 80 -e DEBUG=true <image_id>`
c) `docker run --name myapp -p 80 -e DEBUG=true <container_id>`
e) `docker run --rm --name myapp -p 80 -e DEBUG=true <image_id>`

### Question 11 (weight: 5; total: 60)

A service in a Docker compose file has the following configuration:

```yaml
services:
  myapp:
    image: myapp:latest
    ports:
      - 80:80
    environment:
      DEBUG: "true"
```

How the developer can add a named volume to the service?

a) Add a `volume` key to the service configuration
```
services:
  myapp:
    ...
    volume: "myapp-data:/app"
```
b) Add a `volumes` key to the service configuration
```
services:
  myapp:
    ...
    volumes:
      - myapp-data:/app
```
c) Create a volume service and reference it in the app service
```
services:
  myapp:
    ...
    volumes:
      - myapp-data:/app
  myapp-data:
    type: volume
```
d) Create a volume service and reference the app service in the volume service
```
services:
  myapp:
    ...
  myapp-data:
    type: volume
    services: myapp
```

### Question 12 (weight: 5; total: 65)

The developer has an environment file named `.env` and wants to use it in a Docker compose file. How the developer can use the environment file in the Docker compose file?

a) Add a `env_file` key to the service configuration and reference the `.env` file
b) Add a `environment` key to the service configuration and add the environment variables
c) Just adding the `.env` file in the same directory as the Docker compose file
d) Add a `env` key to the service configuration and reference the `.env` file

### Question 13 (weight: 5; total: 70)

The three main states of a Docker container are:

a) Built, Running, Stopped
b) Created, Running, Paused
c) Created, Running, Stopped
d) Built, Running, Paused

---

## Final Questions

### Question 14 (weight: 15; total: 85)

Based on the Dockerfile below:

```Dockerfile
FROM python:3.11-slim

RUN pip install poetry

WORKDIR /app

COPY . /app

RUN poetry install --only main

EXPOSE 8000
```

Select the correct statements:

[] The base image is `python:3.11-slim`
[] Since `poetry install` commands depends on `pyproject.toml` and `poetry.lock` files and assuming that those files exists, the `poetry install` command will be fail because the `pyproject.toml` and `poetry.lock` files are not being copied to the container
[] Poetry already exists in the base image
[] The container will expose port 8000
[] When the developer runs the container based on the image built from this Dockerfile, the container will automatically bind the container port 8000 to the host port 8000

### Question 15 (weight: 15; total: 100)

Based on the following Docker compose file:

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

networks:
  app-network:
    driver: bridge
```

Select the correct statements:

[] The `app` service will be available at `http://localhost:5432`
[] The `app` service will be available at `http://localhost:8000`
[] The `app` service will run a PostgreSQL database
[] The `app` service will run a Uvicorn application
[] The `postgres` service will be available at `http://localhost:5432`
[] The `postgres` service will be available at `http://localhost:8000`
[] The `postgres` service will run a PostgreSQL database
[] Since the network is a bridge network, the `app` and `postgres` services will be able to communicate with each other using the service name
```