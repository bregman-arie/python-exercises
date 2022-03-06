## Refactor 01

Refactor the following code

```python
from collections import namedtuple

Mushroom = namedtuple('Mushroom', ['name', 'poisonous'])

mushrooms = [Mushroom('Portabello', False), Mushroom('Oyster', False),
             Mushroom('Death Cap', True)]
i = 0

for mushroom in mushrooms:
    i += 1
    name = mushroom.name
    print('%d:"%s"'%(i, name))
```
