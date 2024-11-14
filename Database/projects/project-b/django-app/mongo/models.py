from pydantic import BaseModel, RootModel


class InnerValue(BaseModel):
    name: str
    inner_value: int


class Sample(BaseModel):
    name: str
    values: list[InnerValue]


class Samples(RootModel):
    root: list[Sample]


class Comment(BaseModel):
    content: str
    author: str
    phrase_id: int


class Comments(RootModel):
    root: list[Comment]
