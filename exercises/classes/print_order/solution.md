# Print Order

## Objectives

1. What would be the output of the following code?

```python
print(1)
class Car:
    print(2)
    def __init__(self, color):
        print(3)
        self.color = color
    print(4)
print(5)

car1 = Car("red")
car2 = Car("green")
```

## Solution

1.
```
1
2
4
5
3
3
```

The reason 3 is printed only at the end is because function body isn't executed when it's defined, while class body IS executed when it's defined.