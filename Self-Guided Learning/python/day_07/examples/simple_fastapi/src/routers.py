from fastapi import APIRouter
from src.models import Message

router = APIRouter()


@router.get("/", response_model=Message)
def read_root():
    return {"message": "Hello, World!"}
