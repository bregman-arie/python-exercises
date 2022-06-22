## Type Hinting 101 - Solution

Apply type hinting for each one of the following variables:

1. `x` is a string
2. `y` is an integer
3. `z` is a list of strings
4. `omela` is a function that takes two arguments, both strings and it also returns a string

### Solution

1. `x: str`
2. `y: int`
3.

```python
from typing import List
z: List[str]
```

4.
```python
def omela(x: str, y: str) -> str:
    ...
```
