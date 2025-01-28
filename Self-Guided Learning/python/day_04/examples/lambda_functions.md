# [Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

Lambda functions are small, anonymous functions that can have any number of arguments, but can only have one expression. They are defined using the `lambda` keyword, which is followed by the arguments and a colon, and then the expression to be evaluated.

An anonymous function is a function that is defined without a name. While normal functions are defined using the `def` keyword, lambda functions are defined using the `lambda` keyword.

Lambda functions are often used as a way to create small, throwaway functions that are used only once. They are commonly used in situations where a function is needed for a short period of time, such as when sorting a list or filtering a list of elements.

### Example
```python
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
```

---

## Sorting

Lambda functions can be used to sort a list of tuples based on a specific element of each tuple. The `sort()` method of a list can take a `key` argument, which is a function that is used to determine the sorting order. In this case, a lambda function is used to specify the second element of each tuple as the key for sorting.

### Example
```python
data = [(1, 2), (5, 1), (3, 4), (6, 3)]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(5, 1), (1, 2), (6, 3), (3, 4)]
```

---

## Filtering

Lambda functions can also be used to filter a list of elements based on a specific condition. The `filter()` function can take a lambda function as an argument, which is used to determine whether an element should be included in the filtered list.

### Example
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

---

## Map

Lambda functions can also be used with the `map()` function to apply a function to each element of a list. The `map()` function takes a lambda function and a list as arguments, and returns a new list with the function applied to each element of the original list.

### Example
```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

---

## [Reduce](https://docs.python.org/3/library/functools.html#functools.reduce)

Lambda functions can be used with the `reduce()` function from the `functools` module to apply a function to a list of elements and reduce it to a single value. The `reduce()` function takes a lambda function and a list as arguments, and returns a single value that is the result of applying the function to the elements of the list.

### Example
```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
```
