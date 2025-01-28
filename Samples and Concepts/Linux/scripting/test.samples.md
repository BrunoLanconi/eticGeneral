### Testes de Comparação Numérica:

```bash
#!/bin/bash

# Teste de igualdade
a=5
b=5
if [ "$a" -eq "$b" ]; then
    echo "a é igual a b"
fi

# Teste de maior que
if [ "$a" -gt 3 ]; then
    echo "a é maior que 3"
fi

# Teste de menor que
if [ "$a" -lt 10 ]; then
    echo "a é menor que 10"
fi
```

### Testes de Comparação de Strings:

```bash
#!/bin/bash

# Teste de igualdade de strings
str1="hello"
str2="world"
if [ "$str1" = "$str2" ]; then
    echo "As strings são iguais"
fi

# Teste de strings não nulas
str3="ETIC"
if [ -n "$str3" ]; then
    echo "A string não é nula"
fi
```

### Testes de Arquivos:

```bash
#!/bin/bash

# Teste de existência de arquivo
if [ -e "/etc/passwd" ]; then
    echo "O arquivo /etc/passwd existe"
fi

# Teste de permissão de leitura
if [ -r "/etc/passwd" ]; then
    echo "Você pode ler o arquivo /etc/passwd"
fi
```

### Testes de Variáveis:

```bash
#!/bin/bash

# Teste de variável não nula
var1="Shell Script"
if [ -n "$var1" ]; then
    echo "A variável var1 não é nula"
fi

# Teste de variável nula
var2=""
if [ -z "$var2" ]; then
    echo "A variável var2 é nula"
fi
```

### Testes Combinados:

```bash
#!/bin/bash

# Teste combinado com E lógico
a=10
if [ "$a" -gt 5 -a "$a" -lt 20 ]; then
    echo "a é maior que 5 e menor que 20"
fi

# Teste combinado com Ou lógico
b=30
if [ "$b" -lt 20 -o "$b" -gt 40 ]; then
    echo "b é menor que 20 ou maior que 40"
fi

# Negação lógica
c=100
if ! [ "$c" -lt 50 ]; then
    echo "c não é menor que 50"
fi
```