from datetime import datetime
from typing import Tuple

from pydantic import BaseModel  # type: ignore


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


m = Delivery(timestamp=datetime.now(), dimensions=(10, 20))
print(repr(m.timestamp))
print(m.dimensions)

# NOTE - The following line will raise a validation error:
m = Delivery(timestamp="invalid", dimensions="invalid")  # type: ignore
