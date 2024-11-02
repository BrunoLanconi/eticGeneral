from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.exc import ResourceClosedError
from src.config import config

from models import User

# LINK: https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls
# LINK: https://www.sqlalchemy.org/
# LINK: https://pypi.org/project/psycopg2-binary/
engine = create_engine(
    f"postgresql+psycopg2://{config.postgres_user}:{config.postgres_password}@{config.postgres_host}:{config.postgres_port}/{config.postgres_db}"
)


def _instruction(statement: str, params: dict | None = None) -> list[dict] | None:
    with engine.connect() as connection:
        query = text(statement)
        execution = connection.execute(query, params)

        connection.commit()

        try:
            keys = execution.keys()
            result = execution.fetchall()

            return [dict(zip(keys, row)) for row in result]
        except ResourceClosedError:
            pass

    return None


def _create_statement(statement_prefix: str, **kwargs) -> tuple[str, dict] | None:
    if not all(key in User.model_fields for key in kwargs):
        return None

    params = {key: value for key, value in kwargs.items() if key in User.model_fields}
    statement = (
        statement_prefix
        + " "
        + " AND ".join([f"{key} = :{key}" for key in params.keys()])
    )

    return statement, params


def get_users() -> list[User]:
    results = _instruction("SELECT * FROM users")

    if not results:
        return []

    users = [User(**result) for result in results]

    return users


def get_user(**kwargs) -> User | None:
    result = _create_statement("SELECT * FROM users WHERE", **kwargs)

    if not result:
        return None

    statement, params = result

    result = _instruction(statement=statement, params=params)

    if not result:
        return None

    user = User(**result[0])

    return user


def create_user(user: User) -> User:
    params = user.model_dump()

    _instruction("INSERT INTO users (name, email) VALUES (:name, :email)", params)

    result = get_user(email=user.email)

    if not result:
        raise Exception("User not created")

    return result


def delete_user(**kwargs) -> None:
    result = _create_statement("DELETE FROM users WHERE", **kwargs)

    if not result:
        return None

    statement, params = result

    _instruction(statement=statement, params=params)

    return None


def update_user(id: int, **kwargs) -> User | None:
    user = get_user(id=id)

    if not user:
        return None

    result = _create_statement("UPDATE users SET", **kwargs)

    if not result:
        return None

    statement, params = result
    params["id"] = id

    _instruction(statement + " WHERE id = :id", params)

    return get_user(id=id)


if __name__ == "__main__":
    users = get_users()

    print(users)

    user = get_user(id=1)

    print(user)

    created_user = create_user(User(id=0, name="John Doe", email="test4@gmail.com"))

    print(created_user)

    updated_user = update_user(id=created_user.id, name="Jane Doe")

    print(updated_user)

    delete_user(id=created_user.id)
