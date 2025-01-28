# Lab 05: Dockerfile

Let's create a FastAPI application with a `GET` request and a `POST` request. Also we will create a Dockerfile for a PostgreSQL database and connect it to the FastAPI application. Our `POST` request will insert data into the database and the `GET` request will retrieve data from the database.

## Prerequisites

- Docker installed on your system
- A text editor of your choice

## Instructions

1. Create a new directory for your project:

```bash
mkdir fastapi-postgresql-app
cd fastapi-postgresql-app
```

2. Create a folder called `app`, and a folder `src` on it with a file called `app.py`:

```bash
mkdir app
mkdir app/src
touch app/src/app.py
```
3. Create a simple Python file to handle database operations:

```python
# app/src/db.py

import asyncpg
from src.config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST


async def connect():
    """
    Connects to the PostgreSQL database.

    Returns:
        asyncpg.Connection: The connection object.

    Raises:
        asyncpg.exceptions.PostgresError: If there is an error connecting to the database.
    """
    return await asyncpg.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
        host=POSTGRES_HOST,
    )


async def create_table() -> bool:
    """
    Creates a table named 'items' in the database with the following columns:
        - id: SERIAL PRIMARY KEY
        - name: TEXT NOT NULL
        - description: TEXT NOT NULL

    Returns:
        bool: True if the table is created successfully, False if the table already exists.
    """
    try:
        conn = await connect()

        await conn.execute(
            """
            CREATE TABLE items (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
            """
        )
        await conn.close()

    except asyncpg.exceptions.DuplicateTableError:
        return False
    return True


async def insert_item(name: str, description: str) -> bool:
    """
    Inserts an item into the database.

    Args:
        name (str): The name of the item.
        description (str): The description of the item.
    Returns:
        bool: True if the item was successfully inserted, False otherwise.
    """
    try:
        conn = await connect()

        await conn.execute(
            "INSERT INTO items (name, description) VALUES ($1, $2)", name, description
        )
        await conn.close()

    except asyncpg.exceptions.UndefinedTableError:
        return False
    return True


async def get_items() -> list:
    """
    Retrieves a list of items from the database.

    Returns:
        list: A list of items retrieved from the database.

    Raises:
        asyncpg.exceptions.UndefinedTableError: If the 'items' table does not exist in the database.
    """
    try:
        conn = await connect()
        items: list = await conn.fetch("SELECT * FROM items")

        await conn.close()
        return items

    except asyncpg.exceptions.UndefinedTableError:
        return []

```

4. Create a FastAPI application that includes a `GET` request and a `POST` request:

```python
# app/src/app.py

from fastapi import FastAPI
from src.db import create_table, insert_item, get_items

app = FastAPI()

@app.get('/')
async def read():
    """
    Reads items using the get_items function asynchronously.
    
    Returns:
        items: A list of items.
    """
    items = await get_items()
    
    return items

@app.post('/create')
async def create():
    """
    Asynchronously creates a table and returns the result.
    
    Returns:
        dict: A dictionary containing the result of creating the table.
    """
    result = await create_table()
    
    return {'result': result}

@app.post('/')
async def write():
    """
    Asynchronously writes an item and its description using the `insert_item` function.
    
    Returns:
        dict: A dictionary containing the result of the write operation.
    """
    result = await insert_item('item', 'description')
    
    return {'result': result}
```

5. Initialize a Poetry project on the `app` folder:

```bash
poetry init
```

6. Add FastAPI, asyncpg and Uvicorn as dependencies:

```bash
poetry add fastapi uvicorn asyncpg
```

7. Create a Dockerfile for the FastAPI application:

```Dockerfile
# app/Dockerfile

# Use the official Python image as the base image
FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install --only main

# Expose the port the app runs on
EXPOSE 8000
```

8. Create a folder called `postgres` and a file called `Dockerfile` inside it:

```bash
mkdir postgres
touch postgres/Dockerfile
```

9. Create a Dockerfile for the PostgreSQL database:

```Dockerfile
# postgres/Dockerfile

# Use the official PostgreSQL image as the base image
FROM postgres:14
```

Your project structure should look like this:

```bash
├── Makefile
├── README.md
├── app
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── src
│       ├── app.py
│       └── db.py
└── postgres
    └── Dockerfile
```

10. Now let's create our `config.py` to handle those environment variables:

```python
# app/src/config.py

from decouple import config

# NOTE: We could use Pydantic Settings instead of decouple, but for this example, we will use decou

POSTGRES_USER = config("POSTGRES_USER", cast=str)
"""A string representing the user to connect to the database."""
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
"""A string representing the password to connect to the database."""
POSTGRES_DB = config("POSTGRES_DB", cast=str)
"""A string representing the database to connect to."""
POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
"""A string representing the host to connect to the database."""
```

10. Let's add `python-decouple` to our dependencies:

```bash
poetry add python-decouple
```

11. Build the Docker images:

```bash
docker build -t app app
docker build -t postgres postgres
```

12. Create a network for the containers to communicate:

```bash
docker network create --driver bridge app-network
```

13. Run the PostgreSQL container - remember to add `POSTGRES_USER`, `POSTGRES_PASSWORD` and `POSTGRES_DB` environment variables:

```bash
docker run -d --rm --name postgres --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -p 5432:5432 postgres
```

- `run`: Run a command in a new container
- `-d`: Run the container in the background
- `--rm`: Automatically remove the container when it exits
- `--name postgres`: Assign a name to the container
- `--network app-network`: Connect the container to the `app-network` network
- `-e POSTGRES_USER=postgres`: Set the `POSTGRES_USER` environment variable to `postgres`
- `-p 5432:5432`: Map port 5432 on the host to port 5432 on the container

**Note**: On this command we are not passing a command to run on the container, because the `postgres` image has a default command that starts the PostgreSQL server.

14.  Run the FastAPI application container - remember to add `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_HOST` and `POSTGRES_DB` environment variables:

```bash
docker run -it --rm --name app --network app-network -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_HOST=postgres -e POSTGRES_DB=postgres -v ${PWD}/app:/app -p 8000:8000 app poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000
```

- `-it`: Run the container in interactive mode
- `-v ${PWD}/app:/app`: Mount the `app` directory to the `/app` directory in the container

**Note**: On this command we are passing the command to run on the container, which is `poetry run uvicorn src.app:app --host 0.0.0.0 --port 8000`. Passing a command, overrides the default command specified in the Dockerfile if there is one.

15.  Test the application by sending a `POST` request to `http://localhost:8000/create` and then a `POST` request to `http://localhost:8000/`. Finally, send a `GET` request to `http://localhost:8000/` to retrieve the data from the database.
16.  Stop the containers:

```bash
docker stop app postgres
```
