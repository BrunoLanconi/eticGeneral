1. **Redirecionamento de Saída**:
   - `>`: Redireciona a saída de um comando para um arquivo, substituindo o conteúdo do arquivo se ele já existir.
   - `>>`: Anexa a saída de um comando ao final de um arquivo, preservando o conteúdo existente do arquivo.
   - `2>`: Redireciona a saída de erro (stderr) de um comando para um arquivo.
   - `2>>`: Anexa a saída de erro de um comando ao final de um arquivo.
   - `&>` ou `>&`: Redireciona tanto a saída padrão quanto a saída de erro de um comando para um arquivo.

2. **Redirecionamento de Entrada**:
   - `<`: Redireciona a entrada de um comando para vir de um arquivo.
   - `<<`: Permite a entrada de texto diretamente no terminal até que um delimitador específico seja inserido.

3. **Pipe (Encadeamento de Comandos)**:
   - `|`: Permite encadear a saída de um comando como entrada para outro comando.

4. **Redirecionamento de Descritores de Arquivo**:
   - `n>`: Redireciona o descritor de arquivo n (0 para entrada padrão, 1 para saída padrão e 2 para erro padrão) para um arquivo.
   - `n<`: Redireciona o descritor de arquivo n para a entrada padrão do comando.

5. **Redirecionamento de Saída e Erro para o Mesmo Arquivo**:
   - `&>` ou `>&`: Redireciona tanto a saída padrão quanto a saída de erro de um comando para um arquivo.

6. **Combinação de Comandos**:
   - `&&`: Executa o segundo comando apenas se o primeiro comando for bem-sucedido.
   - `||`: Executa o segundo comando apenas se o primeiro comando falhar.
