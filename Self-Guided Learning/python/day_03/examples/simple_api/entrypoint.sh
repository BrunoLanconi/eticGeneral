#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo "bash - Runs bash"
    echo "fastapi - Runs FastAPI"
    echo "flask - Runs Flask"
}

case ${1} in
bash)
    exec bash
    ;;
fastapi)
    exec poetry run uvicorn src.fastapi_app:app --host 0.0.0.0 --port 5000
    ;;
flask)
    exec poetry run waitress-serve --host 0.0.0.0 --port 5000 src.flask_app:app
    ;;
*)
    print_help
    ;;
esac
