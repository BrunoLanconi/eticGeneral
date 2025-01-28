# [Typing](https://docs.python.org/3/library/typing.html)

`typing` is a module that provides a set of classes and functions to support type hints. It is available in Python 3.5 and later.

---

## Type Hints

Type hints are a way to specify the expected types of function parameters and return values. They are used to improve code readability and catch type errors early in the development process.

### Example
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Type error: Argument 1 to "greet" has incompatible type "int"; expected "str"
print(greet(42))
```

---

## Type Annotations

Type hints are written using type annotations. The following are common type annotations used in Python:

- `int`: Integer

### Example
```python
def add(a: int, b: int) -> int:
    return a + b

print(add(2, 3))  # Output: 5

# Type error: Argument 1 to "add" has incompatible type "str"; expected "int"
print(add("invalid", 3))
```

- `float`: Floating-point number

### Example
```python
def divide(a: float, b: float) -> float:
    return a / b

print(divide(5.0, 2.0))  # Output: 2.5

# Type error: Argument 1 to "divide" has incompatible type "str"; expected "float"
print(divide("invalid", "invalid"))
```

- `str`: String

### Example
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Type error: Argument 1 to "greet" has incompatible type "int"; expected "str"
print(greet(42))
```

- `bool`: Boolean

### Example
```python
def is_even(n: int) -> bool:
    return n % 2 == 0

print(is_even(4))  # Output: True

# Type error: Argument 1 to "is_even" has incompatible type "str"; expected "int"
print(is_even("invalid"))
```

- `List[T]`: List of elements of type `T`

### Example
```python
from typing import List

def double_list(lst: List[int]) -> List[int]:
    return [2 * x for x in lst]

print(double_list([1, 2, 3]))  # Output: [2, 4, 6]

# Type error: Argument 1 to "double_list" has incompatible type "List[str]"; expected "List[int]"
print(double_list(["invalid"]))
```

- `Tuple[T, ...]`: Tuple with elements of type `T`

### Example
```python
from typing import Tuple

def swap(a: int, b: int) -> Tuple[int, int]:
    return b, a

print(swap(1, 2))  # Output: (2, 1)

# Type error: Argument 1 to "swap" has incompatible type "str"; expected "int"
print(swap("invalid", 2))
```

- `Any`: Any type

### Example
```python
from typing import Any

def identity(x: Any) -> Any:
    return x

print(identity(42))  # Output: 42
print(identity("hello"))  # Output: hello
```

- `Literal["value1", "value2", ...]`: Literal type with specific values

### Example
```python
from typing import Literal

def choose(value: Literal["a", "b", "c"]) -> str:
    return f"Chose {value}"

print(choose("a"))  # Output: Chose a

# Type error: Argument 1 to "choose" has incompatible type "d"; expected "Literal['a', 'b', 'c']"
print(choose("d"))
```

---

### Type Aliases

Type aliases are used to define custom types that can be reused throughout the codebase.

### Example
```python
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

new_vector = scale(2.0, [1.0, -4.2, 5.4]) # Output: [2.0, -8.4, 10.8]

# Type error: Argument 1 to "scale" has incompatible type "str"; expected "float"
new_vector = scale("invalid", [1.0, -4.2, 5.4])
```

**Hint**: Instead of using `list[float]`, you can use `List[float]` from the `typing` module, but you need to import it first.

---

### [Type Checking](https://docs.python.org/3/library/typing.html#constant)

Sometimes you may need to use `from __future__ import annotations` to avoid forward reference issues.

### Example
```python
from __future__ import annotations
from typing import TYPE_CHECKING

# A special constant that is assumed to be True by 3rd party static type checkers. It is False at runtime.
if TYPE_CHECKING:
    from mymodule import MyClass

def create_instance() -> MyClass:
    return MyClass()
```

This is useful when you have circular imports or forward references in your code. By using `from __future__ import annotations`, you can avoid these issues, because here `MyClass` is only used for type hinting and not imported at runtime. Basically, `TYPE_CHECKING` is `False` at runtime, so the import is skipped - and `True` during type checking. You can also use `from typing import TYPE_CHECKING` to avoid importing `TYPE_CHECKING` directly.

### Example
```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import expensive_mod

def fun(arg: 'expensive_mod.SomeType') -> None:
    local_var: expensive_mod.AnotherType = other_fun()
```

**Note**: If from `__future__ import annotations` is used, annotations are not evaluated at function definition time. Instead, they are stored as strings in __annotations__. This makes it unnecessary to use quotes around the annotation (see PEP 563).

### Example
```python
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import expensive_mod

def fun(arg: expensive_mod.SomeType) -> None:
    local_var: expensive_mod.AnotherType = other_fun()
```
