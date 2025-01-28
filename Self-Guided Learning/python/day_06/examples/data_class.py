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


p = Point(x=1, y=2, z=3)
print(p)  # Point(x=1, y=2, z=3)
