# Challenge 01: Comprehensions

Translate the given code into comprehensions.

## Materials

- Module: `comprehensions.py`

```python
# comprehension.py

# comprehension.py

iterable = []
for x in range(10):
    iterable.append(x**2)
print(iterable)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

###

iterable = set()
for x in range(10):
    iterable.add(x**2)
print(iterable)  # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

###

iterable = {}
for x in range(10):
    iterable[x] = x**2
print(iterable)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

###

iterable = []
for x in range(10):
    if x % 2 == 0:
        iterable.append(x**2)
print(iterable)  # [0, 4, 16, 36, 64]

###

iterable = map(lambda x: x**2, range(10))
print(list(iterable))  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

###

iterable = []
for x in range(10):
    if x % 2 == 0:
        iterable.append(x**2)
    else:
        iterable.append(x**3)
print(iterable)  # [0, 1, 4, 27, 16, 125, 36, 343, 64, 729]

###

iterable = {}
count = 0
limit = 10

while count < limit:
    iterable[count] = count**2
    count += 1

print(iterable)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

###

iterable = {}

while len(iterable) < 10:
    iterable[len(iterable)] = len(iterable) ** 2

print(iterable)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

## Challenge

- Translate the given code into comprehensions.
