## Type Hinting 102 - Solution

Apply type hinting for each one of the following variables:

1. `abc` is a list of of two integers
2. `qwery` is dictionary where the keys are string and values are integers
3. `elmer` is None but at some point may set as a string
4. `norie` is a variable containing a function that takes two integer arguments and returns a string

### Solution

1.
```
from typing import List

abc: List[int, int]
```

2.
```
from typing import Dict

abc: Dict[str, int]
```

3. 
```
from typing import Optional

elmer: Optional[str]
```

4.
```
from typing import Callable

norie: Callable[[int, int], str]
```
