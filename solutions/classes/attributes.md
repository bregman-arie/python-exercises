## Attributes - Solution

Explain class attributes vs. instance attributes

### Solution

In the following block of code `x` is a class attribute while `self.y` is a instance attribute

```
class MyClass(object):
    x = 1

    def __init__(self, y):
        self.y = y
```
