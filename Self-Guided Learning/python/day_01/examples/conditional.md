## If Statement

The `if` statement is used to execute a block of code if a specified condition is true.

### Example
```python
x = 10

if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5

if x < 5:
    print("x is less than 5")  # This will not be executed
```

---

## Elif Statement

The `elif` statement is used to check multiple expressions for `True` and execute a block of code as soon as one of the conditions is true.

### Example
```python
x = 10

if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is equal to 10")  # Output: x is equal to 10
elif x > 15:
    print("x is greater than 15")
```

---

## Else Statement

The `else` statement is used to execute a block of code if all preceding conditions are false.

### Example
```python
x = 10

if x < 5:
    print("x is less than 5")
elif x > 15:
    print("x is greater than 15")
else:
    print("x is between 5 and 15")  # Output: x is between 5 and 15
```

---

## Nested If Statements

You can use `if` statements inside other `if` statements, which are known as nested `if` statements.

### Example
```python
x = 20
y = 30

if x > 10:
    print("x is greater than 10")
    
    if y > 25:
        print("y is also greater than 25")  # Output: y is also greater than 25
```

---

## Multiple Conditions

You can combine multiple conditions using logical operators (`and`, `or`, `not`).

### Example
```python
x = 20
y = 30

if x > 10 and y > 25:
    print("Both conditions are true")  # Output: Both conditions are true

if x > 10 or y < 25:
    print("At least one condition is true")  # Output: At least one condition is true

if not x < 10:
    print("x is not less than 10")  # Output: x is not less than 10
```

---

## Ternary Conditional Operator

Python also has a ternary conditional operator, which is a one-liner shorthand for the `if-else` statement.

### Example
```python
x = 10

result = "Greater than 5" if x > 5 else "5 or less"
print(result)  # Output: Greater than 5
```
