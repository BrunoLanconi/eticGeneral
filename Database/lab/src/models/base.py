from sqlalchemy.orm import DeclarativeBase

# NOTE: Every new model needs to be added on migrations/env.py and then migrated -> upgraded.
# LINK: python/day_06/examples/database/migrations/env.py#alembic_target_metadata


class Base(DeclarativeBase):
    pass
