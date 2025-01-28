# [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) and Alembic

When dealing with databases in Python, you will often come across two libraries: `SQLAlchemy` and `Alembic`. `SQLAlchemy` is an Object-Relational Mapping (ORM) library that provides a high-level interface for interacting with databases. `Alembic` is a database migration tool that works well with `SQLAlchemy` and helps manage changes to the database schema over time.

### Example
```python
import logging
from sqlalchemy import Column, create_engine
from sqlalchemy.orm import sessionmaker

from src.models.user import User
from src.models.base import Base

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class Database:
    """
    SQLAlchemy database class to manage SQLite database connection and operations with Alembic.
    """

    def __init__(self, db_path: str):
        """
        Initialize the database connection.
        """
        self.db_path = db_path
        self.engine = create_engine(f"sqlite:///{self.db_path}")
        self.Session = sessionmaker(bind=self.engine)

        logger.info(f"Database connection established at {self.db_path}")

    def create_tables(self):
        """
        Create all tables in the database.
        """
        Base.metadata.create_all(self.engine)
        logger.info("All tables created in the database")

    def drop_tables(self):
        """
        Drop all tables from the database.
        """
        Base.metadata.drop_all(self.engine)
        logger.info("All tables dropped from the database")

    def create_user(self, user: User):
        """
        Create a user in the database.
        """
        with self.Session() as session:
            session.add(user)
            session.commit()
            logger.info(f"User {user} created in the database")

    def get_user(self, user_id: int) -> User | None:
        """
        Get a user from the database by its ID.
        """
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            logger.info(f"User {user} retrieved from the database")
            return user

    def delete_user(self, user_id: int):
        """
        Delete a user from the database.
        """
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            session.delete(user)
            session.commit()
            logger.info(f"User {user} deleted from the database")

    def update_user(self, user_id: int, **kwargs):
        """
        Update a user in the database.
        """
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()

            for key, value in kwargs.items():
                if not hasattr(user, key):
                    raise AttributeError(f"User does not have attribute {key}")

                setattr(user, key, value)
            session.commit()
            logger.info(f"User {user} updated in the database")

        return self.get_user(user_id)

    def __enter__(self):
        """
        Enter the context manager.
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit the context manager.
        """
        self.engine.dispose()

```

In the example above, we define a `Database` class that uses `SQLAlchemy` to interact with a SQLite database. The class provides methods to create tables, drop tables, create users, get users, delete users, and update users in the database. It also implements a context manager to manage the database connection.

### Example
```python
from src.models.user import User
from src.db import Database


def main():
    """
    Main function that demonstrates the usage of the Database class.
    The function performs the following steps:
        1. Creates a connection to the SQLite database file "sqlite.db".
        2. Creates necessary tables in the database.
        3. Creates a list of User objects.
        4. Inserts each User object into the database.
        5. Retrieves a user with the ID of 1 from the database.
        6. Prints the retrieved user.
        7. If a user is found, updates the user's name to "John Smith" and deletes the user.
        8. Drops the tables from the database.
    """
    with Database("sqlite.db") as db:
        db.create_tables()

        users = [
            User(name="John Doe"),
            User(name="Jane Doe"),
            User(name="Jack Doe"),
            User(name="Jill Doe"),
        ]

        for user in users:
            db.create_user(user)

        user = db.get_user(1)

        print(user)

        if user:
            db.update_user(user_id=user.id, name="John Smith")
            db.delete_user(user_id=user.id)

        db.drop_tables()


if __name__ == "__main__":
    main()
```

---

## [With Alembic](https://alembic.sqlalchemy.org/en/latest/)

First, Alembic expects that you deal with the database schema in a way that is compatible with migrations. This means that you should not be creating or altering tables directly in the database, but rather define the schema in Python code and use Alembic to generate and apply migrations. That's why we have the `src.models.base.Base` class that inherits from `SQLAlchemy`'s `declarative_base()` function.

### Example
```python
from sqlalchemy.orm import DeclarativeBase

...

class Base(DeclarativeBase):
    pass
```

This `Base` class is used to define the base class for all models in the application. By using this base class, we ensure that all models are compatible with Alembic migrations - and grouping all models under a single base class can be useful for other purposes as well.

### Example
```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class User(Base):
    """
    User model class representing a user in the database.
    
    Since 2.0, SQLAlchemy provides a new way to define mapped attributes using the `mapped_column` function.
    https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#migrating-an-existing-mapping
    
    Attributes:
        id (int): The unique identifier of the user.
        name (str): The name of the user.

    Methods:
        __repr__(): Returns a string representation of the User object.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f"<User(name={self.name})>"
```

In the `User` model class, we define the structure of the `users` table in the database. The `User` class inherits from the `Base` class, which ensures that the model is compatible with Alembic migrations. We define two attributes: `id` and `name`, which represent the unique identifier and name of the user, respectively.

Now that we have defined the models and the database class, we can use Alembic to manage the database schema and migrations. If this is your first time running Alembic, you will need to initialize the Alembic environment by running the following command in the terminal on the root directory of your project:

### Example
```bash
alembic init migrations
```

**Note**: In `python/day_06/examples/database`, we use a `Makefile` to simplify the process of running Alembic commands.

This command will create a new directory called `migrations` that contains the necessary files for managing database migrations. 

### Example
```bash
.
...
├── alembic.ini
├── migrations
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ...
...
```

- `alembic.ini`: The configuration file for Alembic.
- `migrations`: The directory containing the migration scripts.
- `env.py`: The environment configuration file for Alembic.
- `script.py.mako`: The template for generating migration scripts.
- `versions`: The directory containing the migration versions.
- `README`: A README file with information about the migrations directory.

After initializing the Alembic environment, you need to configure `alembic.ini` `alembic.sqlalchemy.url` field and `env.py` `target_metadata` variable.

### Example
```ini
# alembic.ini

[alembic]
...
sqlalchemy.url = sqlite:///sqlite.db
...
```

### Example
```python
# env.py

...
target_metadata = User.metadata
...
```
This configuration tells Alembic what database to use and which models should be migrated (`alembic.sqlalchemy.url` also accepts a list of metadata objects).

Now, you can generate an initial migration script by running the following command:

### Example
```bash
alembic revision --autogenerate -m "Add User table"
```

And apply the migration to the database:

### Example
```bash
alembic upgrade head
```
