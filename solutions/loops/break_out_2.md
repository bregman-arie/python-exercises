## Break Out 2

Iterate over a given list of numbers and break out of it if one the numbers is 2 or 4. If you didn't any of these numbers, print a message saying so.

### Solution

```python
for i in li:
    if i == 2 or i == 4:
        print("Found it!")
        break
else:
    print("Didn't find 2 nor 4")
```
