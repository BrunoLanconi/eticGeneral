# [Data Classes](https://docs.python.org/3/library/dataclasses.html)

Data classes are a way to declare classes that are primarily used to store data. They are similar to namedtuples, but they are mutable and have a lot more features.

### Example
```python
from dataclasses import dataclass


@dataclass
class Point:
    """A point in 3D space."""

    x: int
    y: int
    z: int = 0

    def xyz(self):
        """Return the coordinates of the point."""
        return (self.x, self.y, self.z)
```

Due to the `@dataclass` decorator, the `Point` class is now a data class, and it has some special methods generated automatically. For instance, the `__init__` and `__repr__` are automatically generated as below:

### Example
```python
def __init__(self, x: int, y: int, z: int = 0):
    self.x = x
    self.y = y
    self.z = z

def __repr__(self):
    return f"Point(x={self.x}, y={self.y}, z={self.z})"
```

And you may instantiate the class as below:

### Example
```python
p = Point(x=1, y=2, z=3)
print(p)  # Point(x=1, y=2, z=3)
```

---

## [Arguments](https://docs.python.org/3/library/dataclasses.html#module-contents)

The `@dataclass` decorator has several arguments that you can use to customize the generated methods. For instance:

- `init`: If `True`, an `__init__` method is generated. Default is `True`. The `__init__` method looks like:

### Example
```python
def __init__(self, x: int, y: int, z: int = 0):
    self.x = x
    self.y = y
    self.z = z
```

- `repr`: If `True`, a `__repr__` method is generated. Default is `True`. The `__repr__` method looks like:

### Example
```python
def __repr__(self):
    """The generated repr string will have the class name and the name and repr of each field, in the order they are defined in the class."""
    return f"Point(x={self.x}, y={self.y}, z={self.z})"
```

- `eq`: If `True`, an `__eq__` method is generated. Default is `True`. The `__eq__` method looks like:

### Example
```python
def __eq__(self, other):
    """This method compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type."""
    if other.__class__ is self.__class__:
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)
    return NotImplemented
```

- `order`: If `True`, `__lt__`, `__le__`, `__gt__`, and `__ge__` methods are generated. Default is `False`. The `__lt__` method looks like:

### Example
```python
def __lt__(self, other):
    """This method compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type."""
    if other.__class__ is self.__class__:
        return (self.x, self.y, self.z) < (other.x, other.y, other.z)
    return NotImplemented
```

- `frozen`: If `True`, the class is made immutable. Default is `False`. If you try to change an attribute of an immutable class, a `FrozenInstanceError` is raised.
- `unsafe_hash`: If `True`, a `__hash__` method is generated. Default is `False`. The `__hash__` method looks like:

### Example
```python
def __hash__(self):
    """This method returns a hash based on the hash of the fields of the class."""
    return hash((self.x, self.y, self.z))
```
