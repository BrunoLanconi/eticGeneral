#!/bin/bash

# Criar pasta principal chamada script_sample_folder
mkdir script_sample_folder

# Para cada letra do alfabeto
for letra1 in {a..z}; do
    # Repetir o processo para cada letra do alfabeto
    for letra2 in {a..z}; do
        # Criar uma pasta com o nome da combinação das letras em script_sample_folder
        mkdir "script_sample_folder/$letra1$letra2"
    done
done

# Mensagem de sucesso
echo "Pastas criadas com sucesso."