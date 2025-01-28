## Logical AND (`and`)

The `and` operator returns `True` if both statements are true.

### Example
```python
# Example 1
a = True
b = True

print(a and b)  # Output: True

# Example 2
a = True
b = False

print(a and b)  # Output: False

# Example 3
x = 5
print(x > 3 and x < 10)  # Output: True
```

---

## Logical OR (`or`)

The `or` operator returns `True` if at least one of the statements is true.

### Example
```python
# Example 1
a = True
b = False

print(a or b)  # Output: True

# Example 2
a = False
b = False

print(a or b)  # Output: False

# Example 3
x = 5
print(x > 3 or x < 4)  # Output: True
```

---

## Logical NOT (`not`)

The `not` operator returns `True` if the statement is false, and `False` if the statement is true.

### Example
```python
# Example 1
a = True

print(not a)  # Output: False

# Example 2
b = False

print(not b)  # Output: True

# Example 3
x = 5
print(not(x > 3 and x < 10))  # Output: False
```

---

## Combining Logical Operators

You can combine `and`, `or`, and `not` to form complex conditional statements.

### Example
```python
a = True
b = False
c = True

# Using and, or, not together
result = (a or b) and not c
print(result)  # Output: False

x = 10
y = 5

# Combining logical operators in a complex condition
print((x > 5 and y < 10) or not(x == 10))  # Output: True
```
