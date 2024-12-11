from pydantic import BaseModel, Field, RootModel, field_validator


class InnerValue(BaseModel):
    name: str
    inner_value: int


class Sample(BaseModel):
    name: str
    values: list[InnerValue]


class Samples(RootModel):
    root: list[Sample]


class Comment(BaseModel):
    id: str = Field(alias="_id")
    content: str
    author: str
    phrase_id: int

    @field_validator("id", mode="before")
    @classmethod
    def transform_id(cls, v):
        return str(v)


class Comments(RootModel):
    root: list[Comment]
