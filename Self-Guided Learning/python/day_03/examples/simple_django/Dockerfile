FROM python:3.11-slim

# Install Poetry
RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy the project files
COPY . /app

# Install project dependencies
RUN poetry install --only main

# Migration
RUN poetry run python manage.py migrate

# Run the application
CMD ["poetry", "run", "gunicorn", "setup.wsgi:application", "--bind", "0.0.0.0:5000"]
