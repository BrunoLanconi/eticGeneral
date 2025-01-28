import asyncpg
from src.config import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST


async def connect():
    """
    Connects to the PostgreSQL database.

    Returns:
        asyncpg.Connection: The connection object.

    Raises:
        asyncpg.exceptions.PostgresError: If there is an error connecting to the database.
    """
    return await asyncpg.connect(
        user=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        database=POSTGRES_DB,
        host=POSTGRES_HOST,
    )


async def create_table() -> bool:
    """
    Creates a table named 'items' in the database with the following columns:
        - id: SERIAL PRIMARY KEY
        - name: TEXT NOT NULL
        - description: TEXT NOT NULL

    Returns:
        bool: True if the table is created successfully, False if the table already exists.
    """
    try:
        conn = await connect()

        await conn.execute(
            """
            CREATE TABLE items (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL
            )
            """
        )
        await conn.close()

    except asyncpg.exceptions.DuplicateTableError:
        return False
    return True


async def insert_item(name: str, description: str) -> bool:
    """
    Inserts an item into the database.

    Args:
        name (str): The name of the item.
        description (str): The description of the item.
    Returns:
        bool: True if the item was successfully inserted, False otherwise.
    """
    try:
        conn = await connect()

        await conn.execute(
            "INSERT INTO items (name, description) VALUES ($1, $2)", name, description
        )
        await conn.close()

    except asyncpg.exceptions.UndefinedTableError:
        return False
    return True


async def get_items() -> list:
    """
    Retrieves a list of items from the database.

    Returns:
        list: A list of items retrieved from the database.

    Raises:
        asyncpg.exceptions.UndefinedTableError: If the 'items' table does not exist in the database.
    """
    try:
        conn = await connect()
        items: list = await conn.fetch("SELECT * FROM items")

        await conn.close()
        return items

    except asyncpg.exceptions.UndefinedTableError:
        return []
