1. **Redirecionar saída padrão para um arquivo (substituindo o conteúdo existente)**:
   ```bash
   ls > lista_arquivos.txt
   ```

2. **Redirecionar saída padrão para um arquivo (anexando ao conteúdo existente)**:
   ```bash
   ls >> lista_arquivos.txt
   ```

3. **Redirecionar saída de erro padrão para um arquivo**:
   ```bash
   comando_inexistente 2> erro.log
   ```

4. **Redirecionar saída padrão e de erro para o mesmo arquivo**:
   ```bash
   comando &> output_and_error.log
   ```

5. **Redirecionar saída padrão para a entrada de outro comando (pipe)**:
   ```bash
   ls | grep "arquivo"
   ```

6. **Redirecionar saída padrão para um dispositivo (por exemplo, /dev/null para descartar a saída)**:
   ```bash
   comando > /dev/null
   ```