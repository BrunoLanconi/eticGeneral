from decouple import config

# NOTE: We could use Pydantic Settings instead of decouple, but for this example, we will use decouple.

POSTGRES_USER = config("POSTGRES_USER", cast=str)
"""A string representing the user to connect to the database."""
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
"""A string representing the password to connect to the database."""
POSTGRES_DB = config("POSTGRES_DB", cast=str)
"""A string representing the database to connect to."""
POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
"""A string representing the host to connect to the database."""
