from pydantic_settings import BaseSettings  # type: ignore


class Settings(BaseSettings):
    """
    A class representing the settings for the application.

    Attributes:
        host (str): The host address for the application. Default is "localhost".
        port (int): The port number for the application. Default is 8000.
    """

    host: str = "localhost"
    port: int = 8000


s = Settings()
print(s.host)  # localhost
print(s.port)  # 8000

s = Settings(host="example.com", port=8080)
print(s.host)  # example.com
print(s.port)  # 8080
