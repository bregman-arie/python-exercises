# Attributes

## Objectives

1. Explain class attributes vs. instance attributes
2. True or False? not every object in Python has attributes
3. True or False? An attribute doesn't exist on the variable, but rather on the object that the variable refers to

## Solution

1. In the following block of code `x` is a class attribute while `self.y` is a instance attribute

```
class MyClass(object):
    x = 1

    def __init__(self, y):
        self.y = y
```

2. False. Every object in Python has attributes
3. True
