Para passar argumentos para uma função em um script em shell, você pode acessar esses argumentos dentro da função através das variáveis especiais fornecidas pelo shell. Aqui está como você pode fazer isso:

```bash
minha_funcao() {
    echo "O primeiro argumento é: $1"
    echo "O segundo argumento é: $2"
    echo "Todos os argumentos: $@"
}

minha_funcao argumento1 argumento2
```

- `$1` refere-se ao primeiro argumento passado para a função.
- `$2` refere-se ao segundo argumento passado para a função.
- `$@` refere-se a todos os argumentos passados para a função como uma lista.

```bash
minha_funcao argumento1 argumento2 # Chama a função
```