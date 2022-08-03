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