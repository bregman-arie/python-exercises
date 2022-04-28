## Calculator

Write four functions:

1. Adds the first number to the second one and returns the result
1. Subtracts the second number from the first number and returns the result
1. Multiplies first number by the second number
1. Divides first number by the second number and returns the result

### Solution

1. Adds the first number to the second one and returns the result

```python
def add(x, y)
    """Add numbers"""
    return x + y
```

2. Subtracts the second number from the first number and returns the result

```python
def subtract(x, y)
    """Subtract numbers"""
    return x - y
```

3. Multiplies first number by the second number

```python
def multiply(x, y)
    """Multiply numbers"""
    return x * y
```

4. Divides first number by the second number and returns the result

```python
def divide(x, y)
    """Divide numbers"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y
```
