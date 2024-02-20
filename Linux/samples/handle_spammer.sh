#!/bin/bash

# Verifica se está rodando dentro da pasta script_sample_folder
if [ "$(basename "$PWD")" != "script_sample_folder" ]; then
    # Mensagem de erro
    echo "Erro: Este script deve ser executado dentro da pasta script_sample_folder."
    # Encerra o script
    exit 1
fi

# Verifica se foi passada a letra como argumento
if [ $# -ne 1 ]; then
    # Mensagem de erro
    echo "Erro: Por favor, forneça a letra como argumento."
    # Encerra o script
    exit 1
fi

# Obtém a letra do primeiro argumento
letra="$1"
# Representa todas as pastas que começam com a letra fornecida
pastas="$letra"* 

# Para cada pasta que começa com a letra fornecida
for pasta in $pastas; do
    # Caso seja uma pasta
    if [ -d "$pasta" ]; then
        # Mensagem de log
        echo "Deletando pasta: $pasta"
        # Deleta a pasta
        rm -r "$pasta"
    fi
done

# Mensagem de sucesso
echo "Pastas deletadas com sucesso."
