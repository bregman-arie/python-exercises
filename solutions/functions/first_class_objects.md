## First Class Objects

1. In Python, functions are first-class objects. What does it mean?

### Solution

In general, first class objects in programming languages are objects which can be assigned to variable, used as a return value and can be used as arguments or parameters.<br>
In python you can treat functions this way. Let's say we have the following function

```
def my_function():
    return 5
```

You can then assign a function to a variables like this `x = my_function` or you can return functions as return values like this `return my_function`
