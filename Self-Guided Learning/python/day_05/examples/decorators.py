def uppercase(func):
    print("Uppercase decorator called")

    def wrapper(text):
        result = func(text)
        return result.upper()

    return wrapper


def repeat(n):
    print(f"Repeat decorator called with n={n}")

    def decorator(func):
        def wrapper(*args, **kwargs):
            results = [func(*args, **kwargs) for _ in range(n)]
            return results

        return wrapper

    return decorator


@repeat(3)
@uppercase
def greet(name):
    return f"Hello, {name}!"


print(greet("Alice"))  # Output: ['HELLO, ALICE!', 'HELLO, ALICE!', 'HELLO, ALICE!']
