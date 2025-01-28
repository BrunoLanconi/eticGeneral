from typing import Generator


def my_generator(n: int) -> Generator[int, int, str]:
    """
    A generator function that yields integers from 0 to n-1 and receives values from the caller.
    Args:
        n (int): The upper limit of the range.
    Yields:
        int: The next integer in the range.
    Receives:
        int: The value sent by the caller.
    Return:
        str: A message indicating the last value received.
    """
    for i in range(n):
        x = yield i

        print(f"From caller: {x}")

    return f"The last from caller: {x}"


def main():
    """
    This function demonstrates the usage of a generator.

    It creates a generator object using the `my_generator` function and calls `next()` on it to initialize the generator.
    Then, it enters a loop where it sends a value to the generator using `generator.send()` and increments the value by 10.
    The loop continues until a `StopIteration` exception is raised, at which point the value of the exception is printed.
    """
    generator = my_generator(10)
    next(generator)

    try:
        n = 0
        while True:
            response = generator.send(n)

            print(f"From generator: {response}")

            n += 10

    except StopIteration as e:
        print(e.value)


if __name__ == "__main__":
    main()
