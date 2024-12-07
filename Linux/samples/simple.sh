#!/bin/bash

# Verifica se a pasta "example_folder" existe
if [ ! -d "example_folder" ]; then
    # Cria a pasta "example_folder" se não existir
    mkdir example_folder
    echo "Pasta example_folder criada com sucesso."
else
    # Se a pasta "example_folder" já existe, exibe uma mensagem de aviso
    echo "A pasta example_folder já existe."
fi

# Verifica se o arquivo "example_file.txt" existe
if [ ! -f "example_file.txt" ]; then
    # Cria o arquivo "example_file.txt" se não existir e escreve nele
    echo "Conteúdo inicial" > example_file.txt
    echo "Arquivo example_file.txt criado e conteúdo adicionado."
else
    # Se o arquivo "example_file.txt" já existe, acrescenta conteúdo a ele
    echo "Conteúdo adicional" >> example_file.txt
    echo "Conteúdo adicionado ao arquivo example_file.txt."
fi

# Verifica se o usuário atual possui permissão de escrita no arquivo "example_file.txt"
if [ -w "example_file.txt" ]; then
    # Se o usuário tem permissão de escrita, exibe uma mensagem de sucesso
    echo "Você tem permissão de escrita no arquivo example_file.txt."
else
    # Se o usuário não tem permissão de escrita, exibe uma mensagem de aviso
    echo "Você não tem permissão de escrita no arquivo example_file.txt."
fi
