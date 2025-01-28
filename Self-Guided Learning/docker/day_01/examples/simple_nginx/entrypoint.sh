#!/bin/bash

set -e

function print_help {
    echo "Available options:"
    echo "bash - Runs bash"
    echo "run - Runs NGINX"
}

case ${1} in
bash)
    exec bash
    ;;
run)
    exec nginx -g 'daemon off;'
    ;;
*)
    print_help
    ;;
esac
