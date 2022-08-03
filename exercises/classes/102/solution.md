# Classes 102

## Objectives

1. True or False? 

* Methods are class attributes
* While a function body isn't executed when it's defined, class body is being executed when defined
* When assignments performed in a class, they create variables
* Any function defined in a class is a variable

2. What would be the output of the following code?

```python
print(1)
class Car:
    print(2)
    def __init__(self, color):
        print(3)
        self.color = color
    print(4)
print(5)
```

## Solution

1.

* Methods are class attributes - True
* While a function body isn't executed when it's defined, class body is being executed when defined - True
* When assignments performed in a class, they create variables - False, they create class attributes
* Any function defined in a class is a variable - False, again, it's a class attribute :)

2. The output:

```
1
2
4
5
```
