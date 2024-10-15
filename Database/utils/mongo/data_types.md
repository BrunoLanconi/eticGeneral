## MongoDB Data Types

MongoDB armazena dados em documentos BSON (Binary JSON). BSON é uma representação binária do JSON, com suporte a tipos de dados adicionais.

### [Tipos de Dados BSON](https://www.mongodb.com/pt-br/docs/manual/reference/bson-types/)

Abaixo estão alguns dos tipos de dados BSON mais comuns:

- **Array**: Lista ou matriz de valores.

```json
{
  "array": [1, 2, 3]
}
```

- **Binary Data**: Sequência de bytes.

```json
{
  "binary": BinData(0, "AQIDBA==")
}
```

- **Boolean**: Valor booleano.

```json
{
  "boolean": true
}
```

- **Date**: Data e hora.

```json
{
  "date": ISODate("2021-01-01T00:00:00Z")
}
```

- **Double**: Número de ponto flutuante de 64 bits.

```json
{
  "double": 3.14
}
```

- **JavaScript**: Código JavaScript.

```json
{
  "javascript": "function() { return 'Hello, World!'; }"
}
```

- **Null**: Valor nulo.

```json
{
  "null": null
}
```

- **Object**: Documento BSON incorporado.

```json
{
  "object": {
    "key": "value"
  }
}
```

- **ObjectID**: ID de 12 bytes para o documento.

```json
{
  "object_id": ObjectId("5f5b9e3b3f3b9b0f3f3b9b0f")
}
```

- **Regular Expression**: Expressão regular.

```json
{
  "regex": /pattern/i
}
```

- **String**: Sequência de caracteres Unicode.

```json
{
  "string": "Hello, World!"
}
```

- **Symbol**: Símbolo.

```json
{
  "symbol": Symbol("symbol")
}
```

- **Undefined**: Valor indefinido.

```json
{
  "undefined": undefined
}
```
