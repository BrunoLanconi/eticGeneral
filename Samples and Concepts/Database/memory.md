Quando falamos de programação, a utilização eficiente de memória é um dos pontos mais importantes a serem considerados. Algumas linguagens de programação, como Python, possuem um gerenciamento de memória automático, o que facilita a vida do programador - mas deixando as especificidades de lado, vamos compreender o que ocorre quando declaramos variáveis em um programa ou script, e como a memória é alocada para armazenar esses valores.

## Onde está minha variável?

Durante a execução de um programa, o computador precisa armazenar informações temporárias, como variáveis, para que possa executar as instruções do programa. Para fazer isso, a memória do computador é dividida em diferentes partes, cada uma com uma função específica:

1. **Código**: a parte do programa que contém as instruções a serem executadas.
2. **Dados**: a parte do programa que contém variáveis e estruturas de dados.
3. **Pilha**: a parte da memória que armazena informações sobre as chamadas de função.
4. **Heap**: a parte da memória que é usada para alocar memória dinamicamente.

Quando declaramos uma variável em um programa, a memória é alocada na parte de dados da memória. A quantidade de memória alocada depende do tipo de dado que a variável armazena. Por exemplo, uma variável do tipo `int` (inteiro) geralmente ocupa 4 bytes de memória, enquanto uma variável do tipo `float` (número de ponto flutuante) geralmente ocupa 8 bytes de memória - mas, isto são especificidades técnicas, o que importa é que cada variável ocupa uma quantidade específica de memória e é endereçada em um local específico da memória, que pode ser acessado pelo programa.

```python
>>> x = 42
>>> id(x)
139663296316944
```

Neste exemplo, a variável `x` é alocada na memória e seu endereço é `139663296316944`. Isso significa que o programa pode acessar o valor armazenado em `x` através desse endereço.

```python
>>> def foo():
...     x = 42
...     print(id(y))
...
>>> x = 42
>>> foo()
139663296316944
id(x)
139663296316944
```

Neste exemplo, a variável `x` é alocada na memória fora da função `foo`, enquanto outra variável `x` é alocada dentro da função `foo`. Ambas variáveis têm o mesmo endereço, o que significa que elas apontam para o mesmo local na memória. Isso ocorre porque o Python usa um mecanismo chamado "escopo léxico", que significa que as variáveis são resolvidas em tempo de compilação, e não em tempo de execução.

## Uma outra perspectiva sobre objetos

Em Python, tudo é um objeto. Isso significa que cada variável que declaramos em um programa é, na verdade, uma referência para um objeto na memória. Quando declaramos uma variável, o Python aloca memória para armazenar o objeto correspondente e, em seguida, cria uma referência para esse objeto. Isso significa que, quando passamos uma variável para uma função, estamos passando uma referência para o objeto, não o objeto em si.

```python
>>> def foo(x):
...     x = 42
...     print(id(x))
...
>>> id(x)
>>> y = 10
>>> foo(y)
139790932493840
>>> id(y)
139790932492816
```

A variável `x` dentro da função `foo` é uma referência para o objeto `10` na memória. Quando atribuímos o valor `42` a `x`, estamos criando um novo objeto `42` na memória e fazendo com que `x` aponte para esse novo objeto. No entanto, a variável `y` fora da função `foo` ainda aponta para o objeto `10` original, porque a variável `x` dentro da função `foo` é uma cópia da referência para o objeto `10`, e não a referência em si.