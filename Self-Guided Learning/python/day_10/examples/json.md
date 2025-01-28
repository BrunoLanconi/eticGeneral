# [JSON](https://docs.python.org/3/library/json.html#module-json)

The `json` module provides functions for encoding and decoding JSON data. JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.

---

## [Dump](https://docs.python.org/3/library/json.html#json.dump)

The `json.dump()` function serializes a Python object to a JSON formatted stream. This function takes two arguments: the Python object to serialize and the file-like object to write the JSON data to.

### Example
```python
import json

data = {'key': 'value'}

with open('data.json', 'w') as file:
    json.dump(data, file)
```

---

## [Dumps](https://docs.python.org/3/library/json.html#json.dumps)

The `json.dumps()` function serializes a Python object to a JSON formatted string. This function takes one argument: the Python object to serialize.

### Example
```python
import json

data = {'key': 'value'}
json_string = json.dumps(data)

print(json_string)
```

---

## [Load](https://docs.python.org/3/library/json.html#json.load)

The `json.load()` function deserializes a JSON formatted stream to a Python object. This function takes one argument: the file-like object to read the JSON data from.

### Example
```python
import json

with open('data.json', 'r') as file:
    data = json.load(file)

print(data)
```

---

## [Loads](https://docs.python.org/3/library/json.html#json.loads)

The `json.loads()` function deserializes a JSON formatted string to a Python object. This function takes one argument: the JSON formatted string to deserialize.

### Example
```python
import json

json_string = '{"key": "value"}'
data = json.loads(json_string)

print(data)
```

---

## [Pretty Print](https://docs.python.org/3/library/json.html#json-encoder-and-decoder)

The `json.dumps()` function has additional parameters to control the formatting of the JSON output. The `indent` parameter specifies the number of spaces to use for indentation.

### Example
```python

data = {'key': 'value'}
json_string = json.dumps(data, indent=4)

print(json_string)
```

---

## Sort Keys

The `json.dumps()` function has additional parameters to control the sorting of the keys in the JSON output. The `sort_keys` parameter specifies whether to sort the keys alphabetically.

### Example
```python

data = {'b': 2, 'a': 1}
json_string = json.dumps(data, sort_keys=True)

print(json_string)
```
