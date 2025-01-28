# Lab 04: Develop Your First Script

Now that you have a basic understanding of Python, it's time to create your first script. In this lab, you will write a simple Python script.

## Prerequisites

- Python 3.x installed on your system
- Poetry installed on your system
- A text editor of your choice

## Instructions

1. Create a new project folder named `first_script`.

```bash
mkdir first_script
```

2. Inside the `first_script` folder, initialize a new Python project using Poetry.

```bash
cd first_script
poetry init
```

3. Follow the prompts to create a new `pyproject.toml` file.
4. Create a new Python script file named `main.py` in the `first_script` folder.
5. Open the `main.py` file in your text editor and start writing your script.

## Script Challenge

Write a Python script that:

- Prints a welcome message to the user.
- Has a function that takes a list of fruits as input and prints each fruit name.
- Calls the function with a list of fruits.
- Prints a closing message to the user.

- **Attention**: Remember to `install` and `activate` the virtual environment before running the script.

```bash
poetry install
poetry shell
python main.py
```

- **Attention**: Remember to create a function and call it from `if __name__ == "__main__":`.

### Optional Challenge

- Modify the script to accept user input for the list of fruits.
- Prints all the fruits except the one specified by the user.

**Hint**: You may use [input](https://www.w3schools.com/python/ref_func_input.asp):

```python
fruit = input("What fruit should we remove? ")
print("We should remove " + fruit)
```
