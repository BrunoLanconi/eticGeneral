## Lists
A list is a collection of items that are ordered and changeable. Allows duplicate members.

### Example
```python
# Creating a list
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Adding an item to the list
fruits.append("orange")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Removing an item from the list
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Accessing an item by index
print(fruits[1])  # Output: cherry

# Iterating through the list
for fruit in fruits:
    print(fruit)
```

---

## Tuples
A tuple is a collection of items that are ordered and unchangeable. Allows duplicate members.

### Example
```python
# Creating a tuple
fruits = ("apple", "banana", "cherry")
print(fruits)  # Output: ('apple', 'banana', 'cherry')

# Accessing an item by index
print(fruits[1])  # Output: banana

# Iterating through the tuple
for fruit in fruits:
    print(fruit)

# Tuples are immutable, so we cannot change, add, or remove items
# Trying to do so will result in an error
```

---

## Dictionaries
A dictionary is a collection of items that are unordered, changeable, and indexed. No duplicate members.

### Example
```python
# Creating a dictionary
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing a value by key
print(person["name"])  # Output: John

# Adding a new key-value pair
person["email"] = "john@example.com"
print(person)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'email': 'john@example.com'}

# Removing a key-value pair
person.pop("age")
print(person)  # Output: {'name': 'John', 'city': 'New York', 'email': 'john@example.com'}

# Iterating through the dictionary
for key, value in person.items():
    print(key, value)
```

---

## Sets
A set is a collection of items that are unordered and unindexed. No duplicate members.

### Example
```python
# Creating a set
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'apple', 'banana', 'cherry'}

# Adding an item to the set
fruits.add("orange")
print(fruits)  # Output: {'apple', 'banana', 'orange', 'cherry'}

# Removing an item from the set
fruits.remove("banana")
print(fruits)  # Output: {'apple', 'orange', 'cherry'}

# Sets are unordered, so we cannot access items by index
# Iterating through the set
for fruit in fruits:
    print(fruit)
```

---

## Lists of Dictionaries
Combining lists and dictionaries can create complex data structures.

### Example
```python
# Creating a list of dictionaries
people = [
    {"name": "John", "age": 30},
    {"name": "Jane", "age": 25},
    {"name": "Doe", "age": 35}
]

# Accessing an item in the list and a value in the dictionary
print(people[1]["name"])  # Output: Jane

# Iterating through the list of dictionaries
for person in people:
    print(person["name"], person["age"])
```

---

## Nested Dictionaries
Dictionaries within dictionaries can be used to represent more complex data structures.

### Example
```python
# Creating a nested dictionary
family = {
    "child1": {
        "name": "John",
        "age": 30
    },
    "child2": {
        "name": "Jane",
        "age": 25
    }
}

# Accessing nested dictionary values
print(family["child1"]["name"])  # Output: John

# Iterating through the nested dictionary
for child, info in family.items():
    print(f"{child}: {info['name']} is {info['age']} years old")
```
