FROM python:3.10

# Intall poetry
RUN pip install poetry

# Working directory
WORKDIR /api

# Copy source code
COPY ./src/ ./src/
COPY ./pyproject.toml .
COPY ./README.md .

# Poetry install
RUN poetry install

# # Create requirements
RUN poetry self add poetry-plugin-export
RUN poetry export --without-hashes --format=requirements.txt > requirements.txt

# # Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8001

CMD [ "poetry", "run", "python", "src/main.py" ]