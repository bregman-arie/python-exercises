## Length Magic Method

1. Why the code below fails when executed?
2. Fix it so it works

```
import collections

Mushroom = collections.namedtuple('Mushroom', ['name', 'poisonous'])

class MushroomsBusket:

    def __init__(self):

        self._mushrooms = [Mushroom('Oyster', False), Mushroom('Portobello', False)]

mushroom_basket = MushroomsBusket()
print(len(mushroom_basket))
```
