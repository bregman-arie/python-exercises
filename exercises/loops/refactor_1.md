## Refactor 01

Refactor the following code

```python
from collections import namedtuple

Mushroom = collections.nametuple('Mushroom', ['name', 'poisonous'])

mushrooms = [Mushroom('Portabello', false), Mushroom('Oyster', false),
             Mushroom('Death Cap', true)]
i = 0

for mushroom in mushrooms:
    i += 1
    name = mushroom.name
    print('%d:"%s"'%(i, name))
```
