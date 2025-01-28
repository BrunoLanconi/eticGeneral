# [Generators](https://wiki.python.org/moin/Generators)

Generators are a simple way to create iterators using functions. You can also define iterators using classes, but generators are usually simpler and more elegant.

### Example
```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1

for i in count_up_to(5):
    print(i) # Output: 1 2 3 4 5
```

---

## Generator Expressions

Generator expressions are similar to list comprehensions, but they return an iterator instead of a list. This is useful when you need to iterate over a large dataset without storing the entire list in memory.

### Example
```python
gen = (x ** 2 for x in range(5))
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
print(next(gen))  # Output: 4
print(next(gen))  # Output: 9
print(next(gen))  # Output: 16
```

---

## Built-in Generators - `range()`

The `range()` function is a built-in generator that returns a sequence of numbers. It is commonly used in `for` loops to iterate over a range of values.

### Example
```python
for i in range(5):
    print(i) # Output: 0 1 2 3 4
```

---

## Built-in Generators - `enumerate()`

The `enumerate()` function is another built-in generator that returns a tuple containing the index and value of each element in an iterable.

### Example
```python
for i, char in enumerate('hello'):
    print(i, char) # Output: 0 h, 1 e, 2 l, 3 l, 4 o
```

---

## Built-in Generators - `zip()`

The `zip()` function is a built-in generator that combines two or more iterables into a single iterator of tuples.

### Example
```python
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for item in zip(list1, list2):
    print(item) # Output: (1, 'a'), (2, 'b'), (3, 'c')
```

---

## Built-in Generators - `map()`

The `map()` function is a built-in generator that applies a function to each element in an iterable.

### Example
```python
def square(x):
    return x ** 2

numbers = [1, 2, 3, 4, 5]
squared = map(square, numbers)

for num in squared:
    print(num) # Output: 1 4 9 16 25
```

---

## Built-in Generators - `filter()`

The `filter()` function is a built-in generator that filters elements from an iterable based on a given function.

### Example
```python
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
evens = filter(is_even, numbers)

for num in evens:
    print(num) # Output: 2 4
```
