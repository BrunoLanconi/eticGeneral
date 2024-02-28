1. Alterar o dono de um arquivo para um usuário específico:
```
chown novo_usuario arquivo.txt
```

2. Alterar o grupo de um diretório e todos os seus arquivos para um grupo específico:
```
chown :novo_grupo diretorio/
```

3. Alterar o dono e o grupo de um arquivo para um usuário e um grupo específicos:
```
chown novo_usuario:novo_grupo arquivo.txt
```

4. Recursivamente alterar o dono e o grupo de todos os arquivos em um diretório:
```
chown -R novo_usuario:novo_grupo diretorio/
```

5. Alterar o dono de um link simbólico (sem alterar o arquivo/diretório ao qual ele aponta):
```
chown -h novo_usuario link_simbolico
```

# Trivia

1. **Listar todos os usuários**: Você pode usar o comando `cat` para visualizar o conteúdo do arquivo `/etc/passwd`, que contém informações sobre todos os usuários do sistema. Cada linha neste arquivo representa um usuário.

   ```bash
   cat /etc/passwd
   ```

2. **Listar todos os grupos**: Similarmente, você pode usar o comando `cat` para visualizar o conteúdo do arquivo `/etc/group`, que contém informações sobre todos os grupos do sistema. Cada linha neste arquivo representa um grupo.

   ```bash
   cat /etc/group
   ```
