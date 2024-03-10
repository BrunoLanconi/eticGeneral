# project

Este é o diretório onde ficarão os arquivos do projeto.

## Estrutura de diretórios

```bash
.
├── Makefile
├── README.md
├── api
│   ├── Dockerfile
│   ├── README.md
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── src
│       ├── main.py
│       └── router.py
├── docker-compose.yaml
└── web
    ├── Dockerfile
    ├── README.md
    ├── default.conf
    └── src
        ├── index.html
        ├── script.js
        └── styles.css
```

## Makefile

```bash
api                            Run api container on port 8001
help                           Show help
up                             Run web container on port 8000 and api container on port 8001
web                            Run web container on port 8000
```
