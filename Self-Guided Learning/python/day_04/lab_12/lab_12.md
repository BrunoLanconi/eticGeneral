# Lab 12: Lambda Functions

In this lab, you will get to practice the different use cases of lambda functions in Python and how they can be used to simplify code. You will implement lambda functions to perform the following operations:

- Filter
- Sort
- Map
- Reduce

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

**Attention**: For a better experience, we recommend using a Google Colaboratory notebook or Jupyter notebook to run the code.

1. Create a new directory for this lab and navigate to it.
2. Create a Python script file named `lambda_functions.py`.
3. Implement the following lambda function:

```python
# A lambda function that adds 10 to the number passed in as an argument
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15
```

5. Use lambda functions to sort a list of tuples based on the second element of each tuple. The list of tuples is provided below:

```python
data = [(1, 2), (5, 1), (3, 4), (6, 3)]
data.sort(key=lambda x: x[1])
print(data)  # Output: [(5, 1), (1, 2), (6, 3), (3, 4)]
```

6. Use lambda functions to filter a list of integers and return only the even numbers. The list of integers is provided below:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]
```

7. Use lambda functions with the `map()` function to square each element of a list of integers. The list of integers is provided below:

```python
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```

8. Use lambda functions with the [`reduce()` function](https://docs.python.org/3/library/functools.html#functools.reduce) from the [`functools` module](https://docs.python.org/3/library/functools.html) to calculate the sum of a list of integers. The list of integers is provided below:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15
```

### Optional Challenge

- Use the following list of tuples:

```python
data = [(1, 2), (5, 1), (3, 4), (6, 3), (2, 5), (4, 6), (7, 8), (9, 7), (8, 9), (10, 10), (11, 12)]
```

- Filter the list of tuples to return only the tuples where the sum of the elements is greater than 10 using a lambda function.
- Sort the filtered list based on the second element of the tuples using a lambda function.
- Reduce the filtered list to calculate the product of the first elements of the tuples using a lambda function.
