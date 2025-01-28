1. **Shebang:**
   ```bash
   #!/bin/bash
   ```
   Define o interpretador que será usado para executar o script. No exemplo acima, o script será executado pelo Bash.

2. **Atribuição de Variáveis:**
   ```bash
   VAR="valor"
   ```

3. **Entrada e Saída:**
   ```bash
   echo "Mensagem"    # Exibe uma mensagem na saída padrão
   read VAR          # Lê uma entrada do usuário e a atribui à variável VAR
   ```

4. **Estruturas de Controle:**
   ```bash
   if [ condição ]; then
       comando
   elif [ outra_condição ]; then
       outro_comando
   else
       outro_comando
   fi
   ```
   ```bash
   for VAR in lista; do
       comando
   done
   ```
   ```bash
   while [ condição ]; do
       comando
   done
   ```

5. **Comandos Condicionais:**
   ```bash
   [ condição ]     # Teste condicional
   ```
   ```bash
   [ -f arquivo ]   # Verifica se arquivo existe
   [ -d diretório ] # Verifica se diretório existe
   ```

6. **Redirecionamento e Encadeamento:**
   ```bash
   comando > arquivo.txt   # Redireciona a saída do comando para arquivo.txt (substitui o conteúdo)
   comando >> arquivo.txt  # Anexa a saída do comando ao arquivo.txt
   ```
   ```bash
   comando1 | comando2     # Encadeia a saída do comando1 como entrada para o comando2
   ```

7. **Funções:**
   ```bash
   minha_funcao() {
       comandos
   }
   ```
   ```bash
   minha_funcao  # Chama a função
   ```

8. **Comentários:**
   ```bash
   # Este é um comentário
   ```