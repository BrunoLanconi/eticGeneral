# Lab 08: Python Docker Image

To develop a Python application, you need to have Python installed on your machine. However, you can use Docker to create a Python environment without installing Python on your machine. In this lab, you will create a Docker image that contains Python and run a Python script in a container with Poetry.

## Prerequisites

- Docker
- A text editor of your choice

## Instructions

1. Create a new directory for this lab and navigate to it.
2. Create a new file named `Dockerfile` and add the following content:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry
```

3. Build the image and `bash` into container via `docker run` command:

```bash
docker build -t my-python .
docker run -it --rm -v $(pwd):/app my-python bash
```

4. In the container, run the following commands:

```bash
poetry init
```

5. Since the `-v` flag is used to mount the current directory to the container, you can see the `pyproject.toml` file in the current directory. It will persist, so you can edit your `Dockerfile` to install the dependencies using it:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install
```

6. Write a simple Python script to execute in the container:

```python
# main.py

print("Hello, Python!")
```

7. Edit the `Dockerfile` to run the Python script:

```Dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY . .

RUN poetry install

CMD ["poetry", "run", "python", "main.py"]
```

8. Build the image and run the Python script:

```bash
docker build -t my-python .
docker run -it --rm -v $(pwd):/app my-python
```

### Optional Challenge

- Create a Makefile to simplify the build and run commands.
- Install Make on container and run the Python script using Makefile.
