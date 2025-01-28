class MyContextManager:
    """
    A custom context manager that prints a message when entering and exiting the context.

    Usage:
    with MyContextManager() as result:
        # Code to be executed within the context

    Attributes:
    - None

    Methods:
    - __enter__(): Code to be executed when entering the context.
                   Returns: An object that will be assigned to the 'as' variable.
    - __exit__(exc_type, exc_value, traceback): Code to be executed when exiting the context.
                                                Handles any exceptions raised within the context.
                                                Parameters:
                                                - exc_type: The type of the exception raised.
                                                - exc_value: The value of the exception raised.
                                                - traceback: The traceback of the exception raised.
    """

    def __enter__(self):
        """
        Code to be executed when entering the context.

        Returns:
            str: A greeting message from the context.
        """
        print("Entering the context")
        return "Hello from the context"

    def __exit__(self, exc_type, exc_value, traceback):
        """
        Code to be executed when exiting the context.

        Parameters:
        - exc_type: The type of the exception raised within the context, if any.
        - exc_value: The value of the exception raised within the context, if any.
        - traceback: The traceback of the exception raised within the context, if any.
        """
        print("Exiting the context")

        if exc_type is not None:
            print(f"An exception occurred: {exc_type}, {exc_value}")


def main():
    with MyContextManager() as result:
        print(result)

    with MyContextManager() as result:
        raise ValueError("An error occurred")


if __name__ == "__main__":
    main()
