from pydantic import BaseModel  # type: ignore
import requests  # type: ignore
import urllib.request


class PlaceholderResponse(BaseModel):
    """
    A class to represent a response from the JSONPlaceholder API.
    """

    userId: int
    id: int
    title: str
    completed: bool

    def __str__(self):
        """
        Returns a string representation of the object.

        Returns:
            str: A string representation of the object, including the userId, id, title, and completed status.
        """
        return f"userId: {self.userId}, id: {self.id}, title: {self.title}, completed: {self.completed}"


def main():
    """
    Sends a GET request to the GitHub API and prints the response status code and JSON data.
    """
    response = requests.get("https://api.github.com")

    print(response.status_code)
    print(response.json())

    response = urllib.request.urlopen("https://api.github.com")

    print(response.status)
    print(response.read())

    json_response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
    """
    Sample JSON response:
    {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": false
    }
    """
    placeholder_response = PlaceholderResponse(**json_response.json())

    print(placeholder_response)


if __name__ == "__main__":
    main()
