# Bound to It

## Objectives

Kratos, angry developer, wanted to track the count of how many instances are created out of the class "Car". This is the code he wrote:

```python 
count = 0 
         
         
class Car:
    def __init__(self, color):
        count += 1
        self.color = color
         
         
print(f"Before: {count}")
car = Car("Red")
print(f"After: {count}")
```

1. What's the problem with the code? What exception will it raise?
2. What would you suggest Kratos to fix it?

## Solution

1. In Python a variable inside a function is local. So when we try to increment count inside `__init__` it fails since count isn't assigned with a value. It is NOT the `count` defined above the class `Car`.
The exception raised is `UnboundLocalError`. In other words, you have a local variable that isn't assigned with a variable and you try to access the value of that variable anyway.

2. Use class attributes:

```python         
class Car:
    count = 0

    def __init__(self, color):
        count += 1
        self.color = color
         
         
print(f"Before: {count}")
car = Car("Red")
print(f"After: {count}")
```


Another common solution is to use `global` this way

```python
def __init__(self, color):
        global count
        count += 1
        self.color = color
```

But this is not recommended and it's better to avoid it.