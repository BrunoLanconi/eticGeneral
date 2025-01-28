1. **Uso de pipes para encadear comandos**:
   ```bash
   ls -l | grep "arquivo" | wc -l
   ```
   Este comando lista os arquivos no diretório atual, filtra os que contêm "arquivo" em seus nomes usando `grep` e conta o número de ocorrências usando `wc`.

2. **Uso de && para executar o segundo comando se o primeiro for bem-sucedido**:
   ```bash
   make && sudo make install
   ```
   Este comando compila um programa usando `make` e, se a compilação for bem-sucedida, instala-o com permissões elevadas usando `sudo make install`.

3. **Uso de || para executar o segundo comando se o primeiro falhar**:
   ```bash
   ./script.sh || echo "Script falhou"
   ```
   Este comando executa o script `script.sh` e, se ele falhar (ou seja, retornar um código de saída diferente de zero), exibe a mensagem "Script falhou".

4. **Uso de subshell para redirecionar saída para um arquivo**:
   ```bash
   (ls -l && echo "Listagem concluída") > lista_arquivos.txt
   ```
   Este comando lista os arquivos no diretório atual e, em seguida, adiciona a mensagem "Listagem concluída" ao arquivo `lista_arquivos.txt`.

5. **Uso de `grep` para filtrar saída com base em padrões**:
   ```bash
   ps aux | grep "firefox"
   ```
   Este comando lista todos os processos em execução no sistema e filtra aqueles relacionados ao Firefox.

6. **Uso de `awk` para processamento de texto**:
   ```bash
   ps aux | awk '{print $2, $11}'
   ```
   Este comando lista os IDs de processo e os nomes dos comandos de todos os processos em execução no sistema.