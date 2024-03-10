from fastapi import APIRouter, Request


api_router = APIRouter(
    prefix="/api",
    tags=["api"],
)


@api_router.get("/")
async def get_call(_: Request):
    return {"message": "You successfully GET called the API!"}


@api_router.post("/")
async def post_call(_: Request):
    return {"message": "You successfully POST called the API!"}
