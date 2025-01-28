# Lab 05: Functions and Classes

Since you made your first script in the previous lab, it's time to explore functions and classes in Python.

## Prerequisites

- Python 3.x installed on your system
- Poetry installed on your system
- A text editor of your choice

## Instructions

As you made on the previous lab, create a new project using Poetry. Let's make our script in `main.py`.

## Script Challenge

Write a Python script that:

- Create a class named `Fruit` with the following methods:
  - `__init__`: Initializes the class with a name and a color.
- Create a class named `FruitBasket` with the following methods:
  - `__init__`: Initializes the class with a list
  - `add_fruit`: Adds a fruit to the list
  - `remove_fruit`: Removes a fruit from the list
  - `print_basket`: Prints the list of fruits
- Create a function named `main` that:
  - Creates an instance of the `Fruit` class.
  - Creates an instance of the `FruitBasket` class.
  - Adds the fruit to the basket.
  - Removes the fruit from the basket.
  - Prints the basket content.

- **Attention**: Remember to `install` and `activate` the virtual environment before running the script.

```bash
poetry install
poetry shell
python main.py
```

- **Attention**: Remember to create a function and call it from `if __name__ == "__main__":`.

### Optional Challenge

- Modify the script to accept user input for the fruit name and color.
- Create a for loop to add multiple fruits to the basket.

**Hint**: You may use [input](https://www.w3schools.com/python/ref_func_input.asp):

```python
fruit_name = input("What is the fruit name? ")
fruit_color = input("What is the fruit color? ")
```
