# Lab 09: Simple API

In this lab, you will create a simple API using the `FastAPI` module.

## Prerequisites

- Python 3.x installed on your system
- Poetry installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using a container to isolate the project's dependencies.

1. Create a new directory for this lab and navigate to it.
2. Create a folder named `src` and add a new file named `main.py` with the following content:

```python
# src/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
```

3. Initialize a new Poetry project:

```bash
poetry init
```

4. Add the `fastapi` and `uvicorn` modules as a dependencies:

```bash
poetry add fastapi uvicorn
```

**Note**: The `uvicorn` module is a lightweight ASGI server that can be used to run the FastAPI application.

5. Run the script using Poetry:

```bash
poetry run python src/main.py
```

1. Edit the `pyproject.toml` file to include the `src` folder as a package:

```toml
# pyproject.toml

[tool.poetry]
...
packages = [
    { include = "./src" }
]
...
```

7. Run the FastAPI application using the `uvicorn` module:

```bash
poetry run uvicorn src.main:app --reload
```

8. Open your web browser and navigate to `localhost:8000` to see the API response.

**Attention**: You might notice that `simple_api` sample project has port `5000` exposed. You can change the port by adding the `--port` flag to the `uvicorn` command.

```bash
poetry run uvicorn src.main:app --reload --port 5000
```

### Optional Challenge

- Create a new endpoint that returns a JSON response with a custom message.
- Add a path parameter to the endpoint that captures a value from the URL path.
- Add a query parameter to the endpoint that captures a value from the URL query string.
- Add a request body to the endpoint that captures data from the request body.

### Hero Challenge

- Adapt `simple_api` project `pyproject.toml` file to separate dependencies into flask and fastapi sections. Also remember to adapt the `Dockerfile` to install the correct dependencies.