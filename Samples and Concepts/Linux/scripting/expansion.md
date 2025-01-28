1. **Expansão de Lista**: Você pode especificar uma lista de palavras separadas por espaço dentro de chaves. Por exemplo: `{um,dois,tres}` expandirá para "um dois tres".

2. **Expansão de Caminho**: O Bash expandirá os caracteres curinga (wildcards) como `*` e `?` em nomes de arquivo. Por exemplo, se houver arquivos `arquivo1.txt`, `arquivo2.txt` e `arquivo3.txt` no diretório atual, `arquivo*.txt` será expandido para esses nomes de arquivo.

3. **Expansão de Variáveis**: Você pode expandir o valor de uma variável prefixando-a com o símbolo `$`. Por exemplo, se `nome="João"`, então `$nome` se expandirá para "João".

4. **Expansão Aritmética**: Se você usar a sintaxe `$((expressão))`, o Bash avaliará a expressão aritmética dentro dos parênteses duplos e retornará o resultado. Por exemplo, `$((2 * 3))` se expandirá para 6.

5. **Expansão de Comandos**: Ao usar a sintaxe `$(comando)`, o Bash executará o comando entre parênteses e substituirá a expansão pelo resultado da execução desse comando. Por exemplo, `$(ls)` se expandirá para a lista de arquivos no diretório atual.
