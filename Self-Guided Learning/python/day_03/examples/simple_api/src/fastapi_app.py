from fastapi import FastAPI

from src.fastapi_middlewares import LogMiddleware, ErrorMiddleware, AuthMiddleware

app = FastAPI()


app.add_middleware(AuthMiddleware)
app.add_middleware(ErrorMiddleware)
app.add_middleware(LogMiddleware)


@app.get("/")
async def read_root():
    print("Root")
    return {"message": "Hello, World!"}
