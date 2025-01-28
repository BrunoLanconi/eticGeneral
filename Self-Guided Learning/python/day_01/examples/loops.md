## Basic For Loop

A basic `for` loop iterates over a sequence and executes a block of code for each element.

### Example
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# cherry
```

---

## For Loop with Range

The `range()` function generates a sequence of numbers, which is commonly used with the `for` loop to iterate over a block of code a specified number of times.

### Example
```python
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

---

## For Loop with Range and Start/Stop Parameters

The `range()` function can take a start, stop, and step parameter to control the sequence of numbers generated.

### Example
```python
for i in range(2, 10, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
```

---

## Iterating Over a String

You can use a `for` loop to iterate over each character in a string.

### Example
```python
for char in "hello":
    print(char)

# Output:
# h
# e
# l
# l
# o
```

---

## Iterating Over a Dictionary

When iterating over a dictionary, you can access the keys, values, or key-value pairs.

### Example
```python
student_scores = {"Alice": 90, "Bob": 85, "Charlie": 95}

# Iterating over keys
for student in student_scores:
    print(student)

# Output:
# Alice
# Bob
# Charlie

# Iterating over values
for score in student_scores.values():
    print(score)

# Output:
# 90
# 85
# 95

# Iterating over key-value pairs
for student, score in student_scores.items():
    print(f"{student}: {score}")

# Output:
# Alice: 90
# Bob: 85
# Charlie: 95
```

---

## Using Else with For Loop

The `else` block in a `for` loop is executed after the loop completes all iterations. If the loop is terminated by a `break` statement, the `else` block is not executed.

### Example
```python
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Output:
# 0
# 1
# 2
# 3
# 4
# Loop completed
```

---

## Breaking Out of a For Loop

The `break` statement is used to terminate the loop prematurely when a specific condition is met.

### Example
```python
for i in range(10):
    if i == 5:
        break
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4
```

---

## Continuing to the Next Iteration

The `continue` statement is used to skip the current iteration and proceed to the next iteration of the loop.

### Example
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9
```

---

## Nested For Loops

You can use nested `for` loops to iterate over multiple sequences simultaneously.

### Example
```python
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for a in adj:
    for fruit in fruits:
        print(f"{a} {fruit}")

# Output:
# red apple
# red banana
# red cherry
# big apple
# big banana
# big cherry
# tasty apple
# tasty banana
# tasty cherry
```
