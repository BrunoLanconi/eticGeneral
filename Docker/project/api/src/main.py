from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import api_router
from uvicorn import run


app = FastAPI()

app.include_router(router=api_router)

origins = [
    "http://localhost:8000",
]

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=origins,
    allow_methods=["GET", "POST"],
)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8001)
