# Simple Project

This is a simple project that uses a `Dockerfile` to build an image for a Python application that connects to a PostgreSQL database. The project uses `poetry` to manage dependencies and the `app` directory contains the source code for the application.

```bash
├── Makefile
├── README.md
├── app
│   ├── Dockerfile
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── src
│       ├── app.py
│       ├── config.py
│       └── db.py
├── docker-compose.yaml
└── postgres
    └── Dockerfile
```

## Commands

```bash
build                          Build the project
create-network                 Create a network
help                           Show help
no-compose                     Start the project without docker-compose
up                             Start the project
```