from pydantic_settings import BaseSettings
from pydantic import Field


class Config(BaseSettings):
    postgres_db: str | None = Field(alias="POSTGRES_DB", default=None)
    postgres_host: str | None = Field(alias="POSTGRES_HOST", default=None)
    postgres_password: str | None = Field(alias="POSTGRES_PASSWORD", default=None)
    postgres_port: int | None = Field(alias="POSTGRES_PORT", default=None)
    postgres_user: str | None = Field(alias="POSTGRES_USER", default=None)


config = Config()
