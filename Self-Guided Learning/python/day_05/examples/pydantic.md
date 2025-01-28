# [Pydantic](https://docs.pydantic.dev/latest/)

Pydantic is a data validation and settings management using Python type annotations.

### Example
```python
from datetime import datetime
from typing import Tuple

from pydantic import BaseModel


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])
print(repr(m.timestamp)) # Output: datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions) # Output: (10, 20)
```

---

## Validation

Pydantic uses Python type annotations to validate data. In the example above, the `timestamp` field is expected to be a `datetime` object and the `dimensions` field is expected to be a tuple of two integers. If the data does not match the expected type, Pydantic will raise a `ValidationError`.

### Example
```python
m = Delivery(timestamp="invalid", dimensions="invalid")
"""
Output:
pydantic_core._pydantic_core.ValidationError: 2 validation errors for Delivery
timestamp
  Input should be a valid datetime or date, input is too short [type=datetime_from_date_parsing, input_value='invalid', input_type=str]
    For further information visit https://errors.pydantic.dev/2.8/v/datetime_from_date_parsing
dimensions
  Input should be a valid tuple [type=tuple_type, input_value='invalid', input_type=str]
    For further information visit https://errors.pydantic.dev/2.8/v/tuple_type
"""
```

---

## [Settings Management](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)

Pydantic can also be used to manage settings. In the example below, we define a `Settings` class with default values for `host` and `port`. We can then create an instance of the `Settings` class with the default values or override them with custom values.

**Attention**: `BaseSettings` has been moved to the [pydantic-settings package](https://github.com/pydantic/pydantic-settings). See https://docs.pydantic.dev/2.8/migration/#basesettings-has-moved-to-pydantic-settings for more details.

### Example
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    host: str = "localhost"
    port: int = 8000

s = Settings()
print(s.host) # Output: localhost
print(s.port) # Output: 8000

s = Settings(host="example.com", port=8080)
print(s.host) # Output: example.com
print(s.port) # Output: 8080
```

A nice way to use Pydantic Settings is to [parse environment variables](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#parsing-environment-variable-values). This way, you can easily override the default values with environment variables. For the given environment variables below:

```bash
export V0=0
export SUB_MODEL='{"v1": "json-1", "v2": "json-2"}'
export SUB_MODEL__V2=nested-2
export SUB_MODEL__V3=3
export SUB_MODEL__DEEP__V4=v4
```

You may parse them as:

### Example
```python
from pydantic import BaseModel

from pydantic_settings import BaseSettings, SettingsConfigDict

# Define the nested models
class DeepSubModel(BaseModel):  
    v4: str

# Define the main model
class SubModel(BaseModel):  
    v1: str
    v2: bytes
    v3: int
    deep: DeepSubModel


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='__')

    v0: str
    sub_model: SubModel


print(Settings().model_dump())
"""
Output:
{
    'v0': '0',
    'sub_model': {
        'v1': 'json-1', 
        'v2': b'nested-2', 
        'v3': 3, 
        'deep': {
            'v4': 'v4'
        }
    }
}
"""
```

`v0` is parsed from `V0` as it is. `sub_model` is parsed from `SUB_MODEL`, but `sub_model.v2` defined in `SUB_MODEL` is overridden by `SUB_MODEL__V2`. Since `env_nested_delimiter` is set to '__' and `deep` is parsed as `SUB_MODEL__DEEP` which is a nested model, `sub_model.deep.v4` is parsed from `SUB_MODEL__DEEP__V4`.
