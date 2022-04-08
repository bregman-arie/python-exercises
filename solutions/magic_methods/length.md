## Length Magic Method

1. It will fail because the class MushroomsBasked doesn't implements __len__ magic method

2.

```python
import collections

Mushroom = collections.namedtuple('Mushroom', ['name', 'poisonous'])

class MushroomsBusket:

    def __init__(self):

        self._mushrooms = [Mushroom('Oyster', False), Mushroom('Portobello', False)]

    def __len__(self):
        return len(self._mushrooms)

mushroom_basket = MushroomsBusket()
print(len(mushroom_basket))
```
