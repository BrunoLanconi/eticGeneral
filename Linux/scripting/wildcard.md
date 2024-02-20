# '*'

No contexto do shell do Unix/Linux, o asterisco (*) é um caractere curinga conhecido como "wildcard" ou "globbing". Ele é usado para representar zero ou mais caracteres em um nome de arquivo ou diretório.

Quando você usa o asterisco em um comando, o shell expande automaticamente para corresponder a todos os arquivos e diretórios que seguem o padrão especificado. Por exemplo:

- `*.txt`: corresponde a todos os arquivos com extensão ".txt".
- `file*`: corresponde a todos os arquivos cujos nomes começam com "file".
- `dir*/`: corresponde a todos os diretórios cujos nomes começam com "dir".

A expansão do asterisco ocorre antes que o comando seja executado. O shell examina o diretório atual em busca de nomes de arquivos ou diretórios que correspondam ao padrão especificado e substitui o padrão pelo conjunto de nomes correspondentes antes de passar os argumentos para o comando.

# '?'

O caractere `?` tem um significado especial quando usado em expressões de padrão no contexto de expansão de caminho (globbing) no shell Bash e em outros shells Unix-like. Ele corresponde a qualquer caractere único.

Por exemplo, se você tem arquivos com nomes como `arquivo1.txt`, `arquivo2.txt`, `arquivo3.txt`, etc., e você executa o comando `ls arquivo?.txt`, ele corresponderá a qualquer arquivo que tenha um caractere único após "arquivo" seguido de ".txt". Portanto, neste exemplo, ele corresponderia a `arquivo1.txt`, `arquivo2.txt`, `arquivo3.txt`, mas não a `arquivo10.txt` ou `arquivoXYZ.txt`.

Em resumo, o `?` é usado como um caractere curinga para representar qualquer caractere único em expressões de padrão.