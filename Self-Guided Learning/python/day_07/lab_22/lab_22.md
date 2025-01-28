# Lab 22: API with FastAPI

In this lab, you will create a simple API using FastAPI. This API will cover:

- A single endpoint that returns a JSON response with a message.
- Routers to organize the API endpoints.
- Middleware to log the request and response data.
- Models to define the data structure for the API.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new folder `api-fastapi` and navigate to it.
2. Initialize Poetry in the folder.
3. Install FastAPI and Uvicorn using Poetry.
4. Create a new file `main.py` and add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

5. Run the FastAPI application using Uvicorn:

```bash
poetry run uvicorn main:app --reload
```

6. Open your browser and navigate to `http://localhost:8000`. You should see the message `{"message": "Hello, World!"}` displayed on the page.
7. Create a new file `routers.py` and add the following code:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Hello, World!"}
```

8. Update the `main.py` file to include the router:

```python
from fastapi import FastAPI
from .routers import router

app = FastAPI()

app.include_router(router)
```

9. Create a new file `middleware.py` and add the following code:

```python
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Log Middleware")
        logging.info(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        logging.info(f"Response: {response.status_code}")
        return response
```

10. Update the `main.py` file to include the middleware:

```python
from fastapi import FastAPI
from .routers import router
from .middleware import LogMiddleware

app = FastAPI()

app.add_middleware(LogMiddleware)

app.include_router(router)
```

11. Install Pydantic using Poetry and create a new file `models.py` and add the following code:

```python
from pydantic import BaseModel

class Message(BaseModel):
    message: str
```

12. Update the `routers.py` file to use the model:

```python
from fastapi import APIRouter
from .models import Message

router = APIRouter()

@router.get("/", response_model=Message)
def read_root():
    return {"message": "Hello, World!"}
```

13. Configure the documentation for the API by updating the `main.py` file:

```python
from fastapi import FastAPI
from .routers import router
from .middleware import LogMiddleware

app = FastAPI(
    title="FastAPI Lab",
    description="A simple API using FastAPI",
    version="0.1.0"
)

app.add_middleware(LogMiddleware)

app.include_router(router)
```

14. Run the FastAPI application using Uvicorn:

```bash
poetry run uvicorn main:app --reload
```

15. Open your browser and navigate to `http://localhost:8000/docs`. You should see the FastAPI documentation for the API.

16. You should get an ImportError when running the application.

```
ImportError: attempted relative import with no known parent package
```

**Note**: This error occurs because the `main.py` file is not in a package.

1.  Create a folder `src` and move the `main.py`, `routers.py`, `middleware.py`, and `models.py` files into the folder.
2.  Update `packages` in the `pyproject.toml` file to include the `src` folder:

```toml
...
packages = [
    { include = "src", from = "." }
]
...
```

19. Install the dependencies using Poetry:

```bash
poetry install
```

20. Update all imports to use absolute path from the `src` folder:

```python
from src.routers import router
from src.middleware import LogMiddleware
from src.models import Message
```

21. Run the FastAPI application using Uvicorn:

```bash
poetry run uvicorn src.main:app --reload
```

**Note**: Now `src.main:app` is used to run the FastAPI application.

22. Open your browser and navigate to `http://localhost:8000/docs`. You should see the FastAPI documentation for the API.
23. Open the `/` tab and click on the `Try it out` button. You should see the response with the message `Hello, World!`.