# Simple API

The `FastAPI` module is a Python package for building web APIs. It is a powerful tool that can be used to create complex APIs with minimal effort.

The `Flask` module is another Python package for building web APIs. It is a lightweight alternative to `FastAPI` that is commonly used for building simple APIs.

## Commands

```bash
bash                           Run a bash shell in the Docker container
build                          Build the Docker image
fastapi                        Run the Docker container with FastAPI
flask                          Run the Docker container with Flask
help                           Show help
```

---

## [FastAPI](https://fastapi.tiangolo.com/)

The minimal example of a FastAPI application is as follows:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}
```

---

## [Path Parameters](https://fastapi.tiangolo.com/tutorial/path-params/)

Path parameters are used to capture values from the URL path. They are defined by including a variable in the path string enclosed in curly braces `{}`. The value of the path parameter is extracted from the URL path and passed to the API endpoint as an argument.

### Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

---

### [Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/)

Query parameters are used to pass data to the API endpoint as part of the URL query string. They are defined by including a variable in the endpoint function with a default value.

### Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/")

async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

---

### [Request Body](https://fastapi.tiangolo.com/tutorial/body/)

The request body is used to send data to the API endpoint in the form of JSON. It is defined by including a variable in the endpoint function with the type of the data to be received.

### Example
```python
from fastapi import FastAPI

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return {"item_name": item.name, "item_price": item.price}
```

---

## [Routers](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

Routers are used to organize API endpoints into separate modules. They are defined by creating a new instance of the `APIRouter` class and adding endpoints to it.

### Example
```python
from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@router.get("/")
async def read_root():
    return {"message": "Hello, World!"}

app.include_router(router)
```

In this case, the URL for the endpoint is `http://localhost:8000/`.

You may use the `prefix` parameter to specify a common path prefix for all endpoints in the router.

### Example
```python
...
app.include_router(router, prefix="/items")
...
```

In this case, the URL for the endpoint is `http://localhost:8000/items/`.

Routers may also be nested to create a hierarchy of endpoints.

### Example
```python
...
router = APIRouter()

...

nested_router = APIRouter()

@nested_router.get("/")
async def read_nested():
    return {"message": "Hello, Nested World!"}

router.include_router(nested_router, prefix="/nested")
app.include_router(router, prefix="/items")
```

In this case, the URL for the endpoint is `http://localhost:8000/items/nested/`.

---

## [Middleware](https://fastapi.tiangolo.com/tutorial/middleware/)

Middleware functions are used to intercept requests and responses to perform additional processing. They are defined by creating a function that takes a `Request` object and a `Callable` object as arguments.

### Example
```python
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Process-Time"] = "0.123"
    return response
```

The code above adds a CORS middleware to the application and a custom middleware that adds a `X-Process-Time` header to the response.

---

## [Custom Middleware](https://fastapi.tiangolo.com/advanced/middleware/)

Custom middleware functions can be created by defining a class that inherits from the `BaseHTTPMiddleware` class and implementing the `dispatch` method.

### Example
```python
from fastapi import FastAPI, Request
from fastapi.middleware.base import BaseHTTPMiddleware

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        response.headers["X-Custom-Header"] = "Custom Value"
        return response

app = FastAPI()
app.add_middleware(CustomMiddleware)
```

The code above creates a custom middleware class that adds a `X-Custom-Header` header to the response.

You may use custom middleware to perform additional processing on requests and responses, such as authentication, logging, or error handling.

### Example
```python
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Auth Middleware")
        if not request.headers.get("Authorization"):
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        # Do something with the Authorization header

        response = await call_next(request)
        return response


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Log Middleware")
        logging.info(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        logging.info(f"Response: {response.status_code}")
        return response


class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Error Middleware")

        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=500, content={"message": "Internal Server Error"}
            )


app = FastAPI()

app.add_middleware(AuthMiddleware)
app.add_middleware(ErrorMiddleware)
app.add_middleware(LogMiddleware)
```

The order in which middleware is added to the application is important, as middleware functions are executed **reversed** the order they are added. In the example above, the `LogMiddleware` will be executed first, followed by the `ErrorMiddleware`, and finally the `AuthMiddleware`.

Middlewares usually uses `call_next` to pass the request to the next middleware in the chain. In some middleware paths, when what is being returned is `JSONResponse` and not the `call_next`, that means the chain should be broken and the response should be returned immediately. If the complete chain is executed, the last `call_next` will evoke the endpoint function.

For instance, if we try to `GET` the `/` endpoint, the output will be as follows:

```
Log Middleware
Error Middleware
Auth Middleware
INFO:     172.17.0.1:56282 - "GET / HTTP/1.1" 401 Unauthorized
```

---

# [Models](https://fastapi.tiangolo.com/tutorial/body/#create-a-request-body)

Models are used to define the structure of the data that is sent to or received from the API endpoints. They are defined by creating a class that inherits from the `BaseModel` class and adding attributes with type annotations.

### Example
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
```

The code above creates a model class `Item` with two attributes `name` and `price` of type `str` and `float`, respectively.

Models can be used as request bodies to receive data from the client or as response bodies to send data to the client.

### Example
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):   
    return {"item_name": item.name, "item_price": item.price}
```

The code above creates an endpoint that receives an `Item` object as a request body and returns the `name` and `price` attributes of the object in the response.

---

## [Flask](https://flask.palletsprojects.com/)

The equivalent Flask application for the FastAPI example is as follows:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"message": "Hello, World!"})
```

Run the Flask application using the following command:

```bash
export FLASK_APP=app.py
flask run
```
