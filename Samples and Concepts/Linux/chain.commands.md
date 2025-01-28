1. **Redirecionamento de Saída:**
   - **>**: Redireciona a saída de um comando para um arquivo, substituindo o conteúdo do arquivo se ele já existir.
     Exemplo: `ls > lista_arquivos.txt` - redireciona a saída do comando `ls` para o arquivo `lista_arquivos.txt`.
   - **>>**: Anexa a saída de um comando ao final de um arquivo, preservando o conteúdo existente do arquivo.
     Exemplo: `ls >> lista_arquivos.txt` - anexa a saída do comando `ls` ao final do arquivo `lista_arquivos.txt`.
   - **2>**: Redireciona a saída de erro (stderr) de um comando para um arquivo.
     Exemplo: `ls arquivos_inexistentes 2> erros.txt` - redireciona os erros do comando `ls` para o arquivo `erros.txt`.
   - **2>>**: Anexa a saída de erro de um comando ao final de um arquivo.
     Exemplo: `ls arquivos_inexistentes 2>> erros.txt` - anexa os erros do comando `ls` ao final do arquivo `erros.txt`.
   - **&> ou >&**: Redireciona tanto a saída padrão quanto a saída de erro de um comando para um arquivo.
     Exemplo: `ls &> saida_e_erros.txt` - redireciona a saída padrão e os erros do comando `ls` para o arquivo `saida_e_erros.txt`.

2. **Redirecionamento de Entrada:**
   - **<**: Redireciona a entrada de um comando para vir de um arquivo.
     Exemplo: `sort < lista_numeros.txt` - usa o arquivo `lista_numeros.txt` como entrada para o comando `sort`.
   - **<<**: Permite a entrada de texto diretamente no terminal até que um delimitador específico seja inserido.
     Exemplo: `cat << FIM` - permite a entrada de texto até que a palavra `FIM` seja inserida.

3. **Pipe (Encadeamento de Comandos):**
   - **|**: Permite encadear a saída de um comando como entrada para outro comando.
     Exemplo: `ls | grep "arquivo"` - lista os arquivos do diretório atual e filtra apenas aqueles que contêm "arquivo" em seus nomes.

4. **Combinação de Comandos:**
   - **&&**: Executa o segundo comando apenas se o primeiro comando for bem-sucedido.
     Exemplo: `make && make install` - compila e instala um programa apenas se a compilação for bem-sucedida.
   - **||**: Executa o segundo comando apenas se o primeiro comando falhar.
     Exemplo: `command1 || command2` - executa `command2` apenas se `command1` falhar.