# Project B

## Overview

Project B is a Django-based application. This repository contains all the necessary files to build, run, and manage the project.

## Project Structure

```
.
├── Makefile
├── data.json
├── django-app
│   ├── README.md
│   ├── manage.py
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── setup
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── docker-compose.yaml
└── ops
  └── django-app.Dockerfile
```

## Makefile Commands

- `bash`: Run bash in the django-app container
- `build`: Build the project
- `dump`: Dump the database
- `help`: Show help
- `load`: Load the database
- `migrate`: Run migrations
- `up`: Run the project

## Getting Started

1. **Build the project:**
   ```sh
   make build
   ```

2. **Run the project:**
   ```sh
   make up
   ```

3. **Run migrations:**
   ```sh
   make migrate
   ```

4. **Dump the database:**
   ```sh
   make dump
   ```

5. **Load the database:**
   ```sh
   make load
   ```

6. **Run bash in the django-app container:**
   ```sh
   make bash
   ```

  ## Docker Services

  This project uses Docker to manage its services. Below is a brief overview of the services defined in the `docker-compose.yaml` file:

  ### Database

  - **Image**: postgres
  - **Restart Policy**: always
  - **Volumes**: 
    - `data:/var/lib/postgresql/data`
  - **Environment Variables**:
    - `POSTGRES_PASSWORD`: password
    - `POSTGRES_USER`: user
    - `POSTGRES_DB`: db
  - **Networks**: 
    - `app-network`

  ### Django App

  - **Build Context**: `./django-app`
  - **Dockerfile**: `../ops/django-app.Dockerfile`
  - **Ports**: 
    - `8000:8000`
  - **Command**: 
    ```sh
    bash -c "poetry run python manage.py migrate && poetry run gunicorn -w 20 -b 0.0.0.0:8000 setup.wsgi"
    ```
  - **Environment Variables**:
    - `POSTGRES_PASSWORD`: password
    - `POSTGRES_USER`: user
    - `POSTGRES_DB`: db
    - `POSTGRES_HOST`: database
    - `POSTGRES_PORT`: 5432
  - **Networks**: 
    - `app-network`
  - **Depends On**: 
    - `database`

  ### Adminer

  - **Image**: adminer
  - **Restart Policy**: always
  - **Links**: 
    - `database:db`
  - **Ports**: 
    - `5433:8080`
  - **Networks**: 
    - `app-network`
  - **Depends On**: 
    - `database`

  ### Volumes

  - `data`

  ### Networks

  - `app-network` (driver: bridge)

## Attention Points

1. Garanta que os serviços listados no `docker-compose.yaml` estão sob a mesma network, que deverá estar em modo bridge.

```
networks:
  app-network:
    driver: bridge
```

2. Garanta que o serviço `django` tem as variáveis de ambiente sendo injetadas de acordo e que essas variáveis estão sendo utilizadas no arquivo `settings.py`.

```
# POSTGRES_DB = os.environ.get("POSTGRES_DB")
POSTGRES_DB = config("POSTGRES_DB", cast=str)
POSTGRES_HOST = config("POSTGRES_HOST", cast=str)
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD", cast=str)
# POSTGRES_PORT = int(None)
POSTGRES_PORT = config("POSTGRES_PORT", cast=int)
POSTGRES_USER = config("POSTGRES_USER", cast=str)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": POSTGRES_DB,
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": POSTGRES_HOST,
        "PORT": POSTGRES_PORT,
    }
}
```

3. (Opcional) Garanta que o serviço `adminer` está linkado ao serviço `database`.

```
links:
  - database:db
```

## License

This project is licensed under the MIT License.