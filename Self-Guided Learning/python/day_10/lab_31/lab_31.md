# Lab 31: Requests

In this lab, you will learn how to make HTTP requests in Python. You will create a function that makes a GET request to a URL and prints the response content.

## Prerequisites

- Python 3.x installed on your system
- A text editor of your choice

## Instructions

1. Create a new Python file called `main.py`.
2. Create a function called `get_url` that makes a GET request to a URL and prints the response content.

```python
import requests

def get_url(url: str) -> None:
    """
    Make a GET request to a URL and print the response content.

    Args:
        url (str): The URL to make the request to.
    """
    response = requests.get(url)
    print(response.text)

get_url('https://www.google.com')
```

3. Run the Python file and observe the output.
4. Create a function called `post_url` that makes a POST request to a URL with a payload and prints the response content.

```python
def post_url(url: str, payload: dict) -> None:
    """
    Make a POST request to a URL with a payload and print the response content.

    Args:
        url (str): The URL to make the request to.
        payload (dict): The payload to send in the request.
    """
    response = requests.post(url, data=payload)
    print(response.text)

post_url('https://httpbin.org/post', {'key': 'value'})
```

5. Run the Python file and observe the output.
6. Now let's create a function called `get_json` that makes a GET request to a URL and returns the response JSON content.

```python
def get_json(url: str) -> dict:
    """
    Make a GET request to a URL and return the response JSON content.

    Args:
        url (str): The URL to make the request to.

    Returns:
        dict: The JSON content of the response.
    """
    response = requests.get(url)
    return response.json()

print(get_json('https://jsonplaceholder.typicode.com/posts/1'))
```

7. Run the Python file and observe the output.
8. Create a Pydantic model called `Post` with the following fields: `userId`, `id`, `title`, and `body`.

```python
from pydantic import BaseModel

class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str
```

9. Change the `get_json` function to return a `Post` object instead of a dictionary.

```python
def get_json(url: str) -> Post:
    """
    Make a GET request to a URL and return the response JSON content as a Post object.

    Args:
        url (str): The URL to make the request to.

    Returns:
        Post: The Post object representing the JSON content of the response.
    """
    response = requests.get(url)
    return Post(**response.json())

print(get_json('https://jsonplaceholder.typicode.com/posts/1'))
```

10. Run the Python file and observe the output.
11. Create a `__str__` method in the `Post` class that returns a formatted string representation of the object.

```python
class Post(BaseModel):
    userId: int
    id: int
    title: str
    body: str

    def __str__(self) -> str:
        return f'Post(userId={self.userId}, id={self.id}, title={self.title}, body={self.body})'
```

12. Run the Python file and observe the output.

### Optional Challenge

- Create a function called `get_image` that makes a GET request to a URL and saves the image content to a file.