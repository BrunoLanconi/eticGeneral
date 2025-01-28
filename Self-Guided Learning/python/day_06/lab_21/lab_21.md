# Lab 21: SQLAlchemy Model

In this lab, you will create a SQLAlchemy model to represent a `Company` with attributes:

- `name` (str)
- `location` (str)
- `industry` (str)
- `headcount` (int)

Create a revision and migrate the model to a SQLite database using Alembic.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Note**: Use the `python/day_06/examples/database` project - in that way, you may only add the `Company` model class and the necessary Alembic commands.

1. Create a new Python file called `company.py` in the `models` directory.
2. In `models/company.py`, create a SQLAlchemy model class called `Company` with four attributes: `name` (str), `location` (str), `industry` (str), and `headcount` (int).

```python
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base


class Company(Base):
    """
    Company model class representing a company in the database.
    
    Since 2.0, SQLAlchemy provides a new way to define mapped attributes using the `mapped_column` function.
    https://docs.sqlalchemy.org/en/20/changelog/whatsnew_20.html#migrating-an-existing-mapping
    
    Attributes:
        id (int): The unique identifier of the company.
        name (str): The name of the company.
        location (str): The location of the company.
        industry (str): The industry of the company.
        headcount (int): The number of employees in the company.

    Methods:
        __repr__(): Returns a string representation of the Company object.
    """

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    industry: Mapped[str] = mapped_column(String)
    headcount: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"<Company(name={self.name}, location={self.location}, industry={self.industry}, headcount={self.headcount})>"
```

3. In `migration/env.py`, import the `Company` model class and add it to the `target_metadata` variable.

```python
...

from src.models.company import Company

...

target_metadata = [
    User.metadata,
    Company.metadata,
]

...
```

4. Create a new revision using Alembic with the following command:

```bash
poetry run alembic revision --autogenerate -m "Add Company model"
```

5. Migrate the revision to the SQLite database with the following command:

```bash
poetry run alembic upgrade head
```

6. Verify that the `companies` table has been created in the SQLite database.


### Optional Challenge

- Create another model class called `Employee` with attributes: `name` (str), `position` (str), `salary` (float), and `company_id` (int).
- Add a foreign key relationship between the `Employee` and `Company` models.
- Create a new revision and migrate the `Employee` model to the SQLite database.