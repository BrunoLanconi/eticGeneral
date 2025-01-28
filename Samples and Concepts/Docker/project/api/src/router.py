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


@api_router.get("/birds")
async def get_birds(_: Request):
    return [
        {
            "name": "Eagle",
            "data": {"color": "Brown", "age": 5, "weight": 5.5},
            "img": "https://cdn.pixabay.com/photo/2014/11/29/19/33/bald-eagle-550804_1280.jpg",
        },
        {
            "name": "Sparrow",
            "data": {"color": "Brown", "age": 1, "weight": 0.5},
            "img": "https://cdn.pixabay.com/photo/2018/12/25/20/11/sparrow-3894775_1280.jpg",
        },
        {
            "name": "Parrot",
            "data": {"color": "Green", "age": 2, "weight": 0.7},
            "img": "https://cdn.pixabay.com/photo/2017/03/12/23/31/kea-2138420_960_720.jpg",
        },
    ]
