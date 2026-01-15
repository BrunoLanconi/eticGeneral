# little_lab

Small Node.js “lab” project for experimenting with JavaScript concepts in an isolated environment (local Node or Docker).

## What’s inside

```
.
├─ src/
│  └─ index.js
├─ package.json
├─ Dockerfile
├─ docker-compose.yaml
├─ Makefile
└─ README.md
```

`src/index.js` is the main entry point.

## Requirements

Choose one:

- **Local**: Node.js + npm
- **Containerized**: Docker + Docker Compose

## Run locally

Install dependencies:

```bash
npm install
```

Run:

```bash
npm start
```

If `start` isn’t defined in `package.json`, run directly:

```bash
node src/index.js
```

## Run with Docker

Build the image:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

Stop:

```bash
docker compose down
```

## Makefile helpers

If a `Makefile` is provided, list targets with:

```bash
make help
```

Available targets:

```bash
bash                           Open a bash shell in the running Docker container
help                           Show help
init                           Initialize npm in the project
start                          Start the JavaScript application
test                           Run tests for the JavaScript application
```

## Notes

- Edit and add experiments in `src/index.js` (or create new files under `src/`).
- Keep the lab small and focused; commit experiments as separate steps when possible.