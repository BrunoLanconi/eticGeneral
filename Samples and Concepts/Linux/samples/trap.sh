#!/bin/bash

# Definir uma função para manipular o sinal SIGTERM
trap 'echo "Sinal SIGINT recebido. Encerrando o script..."; exit' SIGINT

# Iniciar a execução do script
echo "Script em execução..."

# Aguardar indefinidamente (ou até receber um sinal SIGTERM)
while true; do
    sleep 1
    echo "Aguardando..."
done