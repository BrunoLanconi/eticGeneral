### **1. Object:**
- **Atributos:**
  - `Object.prototype`: Permite adicionar propriedades e métodos ao objeto `Object`.
- **Métodos:**
  - `Object.create()`: Cria um novo objeto com um protótipo especificado.
  - `Object.keys()`: Retorna uma matriz contendo os nomes das propriedades de um objeto.
  - `Object.values()`: Retorna uma matriz contendo os valores das propriedades de um objeto.
  - `Object.entries()`: Retorna uma matriz contendo pares chave/valor em forma de arrays.

### **2. Array:**
- **Atributos:**
  - `Array.prototype.length`: Retorna ou define o número de elementos em um array.
- **Métodos:**
  - `Array.isArray()`: Verifica se um objeto é uma matriz.
  - `Array.from()`: Cria uma nova instância de array a partir de um objeto semelhante a uma matriz ou iterável.
  - `Array.prototype.push()`: Adiciona um ou mais elementos ao final de um array.
  - `Array.prototype.pop()`: Remove o último elemento de um array.

### **3. Function:**
- **Atributos:**
  - `Function.prototype`: Permite adicionar propriedades e métodos ao objeto `Function`.
- **Métodos:**
  - `Function.prototype.apply()`: Chama uma função com um dado `this` e argumentos fornecidos como uma matriz.
  - `Function.prototype.call()`: Chama uma função com um dado `this` e argumentos fornecidos individualmente.
  - `Function.prototype.bind()`: Cria uma nova função que, quando chamada, tem seu `this` configurado com um valor específico.

### **4. String:**
- **Atributos:**
  - `String.prototype.length`: Retorna o número de caracteres em uma string.
- **Métodos:**
  - `String.prototype.indexOf()`: Retorna o índice da primeira ocorrência de uma substring.
  - `String.prototype.slice()`: Extrai uma parte da string e retorna uma nova string.
  - `String.prototype.toUpperCase()`: Converte a string para maiúsculas.
  - `String.prototype.toLowerCase()`: Converte a string para minúsculas.

### **5. Number:**
- **Atributos:**
  - `Number.prototype`: Permite adicionar propriedades e métodos ao objeto `Number`.
- **Métodos:**
  - `Number.isNaN()`: Verifica se um valor é NaN (Não é um número).
  - `Number.toFixed()`: Formata um número usando notação de ponto fixo.

### **6. Math:**
- **Métodos:**
  - `Math.abs()`: Retorna o valor absoluto de um número.
  - `Math.random()`: Retorna um número pseudoaleatório entre 0 (inclusive) e 1 (exclusive).
  - `Math.floor()`: Arredonda para baixo um número para o inteiro mais próximo.

### **7. Date:**
- **Métodos:**
  - `Date.now()`: Retorna o número de milissegundos desde 1º de janeiro de 1970 (Época UNIX).
  - `Date.prototype.getFullYear()`: Retorna o ano de uma data como um número de quatro dígitos.
  - `Date.prototype.getMonth()`: Retorna o mês de uma data como um número (0 a 11).
