# Lab 04: Contained App

Now that you know how to build and run a container, let's create a containerized FastAPI application with Poetry. In this lab, you'll create a FastAPI application, build a Docker image, and run a container with the FastAPI application.

## Prerequisites

- Docker installed on your system
- A text editor of your choice

## Instructions

1. Create a new directory for your FastAPI application:

```bash
mkdir fastapi-app
cd fastapi-app
```

2. Initialize a new Poetry project:

```bash
poetry init
```

3. Add FastAPI and Uvicorn as dependencies:

```bash
poetry add fastapi uvicorn
```

4. Create a new Python file for your FastAPI application:

```bash
touch main.py
```

5. Add the following code to `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

6. Run the FastAPI application with Uvicorn:

```bash
poetry run uvicorn main:app --reload
```

7. Open your browser and navigate to `http://localhost:8000`. You should see the message `{"Hello": "World"}`.
8. Stop the FastAPI application by pressing `Ctrl+C`.
9. Create a new file named `Dockerfile`:

```bash
touch Dockerfile
```

10. Add the following code to `Dockerfile`:

```Dockerfile
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install --only main

# Entrypoint
RUN chmod a+x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
```

11. Create a new file named `entrypoint.sh`:

```bash
#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo "bash - Runs bash"
    echo "fastapi - Runs FastAPI"
    echo "flask - Runs Flask"
}

case ${1} in
bash)
    exec bash
    ;;
fastapi)
    exec poetry run uvicorn main:app --host 0.0.0.0 --port 8000
    ;;
*)
    print_help
    ;;
esac
```

12. Build the Docker image:

```bash
docker build -t fastapi-app .
```

13. Run the Docker container:

```bash
docker run -it --rm -p 8000:8000 fastapi-app fastapi
```

14. Open your browser and navigate to `http://localhost:8000`. You should see the message `{"Hello": "World"}`.
15. Stop the Docker container by pressing `Ctrl+C`.
16. Run the Docker container with a different command:

```bash
docker run -it --rm fastapi-app bash
```

17. You should now be inside the Docker container. Run the following command to start the FastAPI application:

### Optional Challenge

- Create a Python script that consumes the FastAPI application. Try using another container to run the script and interact with the FastAPI application. The challenge is to explore how containers can communicate with each other.