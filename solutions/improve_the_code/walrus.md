## Walrus

Modify the following code so it will use the walrus operator:

```python
x = 50
y = x - 20
if y == 30:
    print("super")
```

### Solution

```python
x = 50
if y := x - 20 == 30:
   print("super")
```
