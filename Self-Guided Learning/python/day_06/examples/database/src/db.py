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
