## Start with a Letter

1. How to check if a string starts with a letter?

### Solution

```python

# Regex based solution
import re
if re.match("^[a-zA-Z]+.*", string):
    print("yay, it starts with a letter")

# Built-in string method
if string and string[0].isalpha():
    print("yay, it starts with a letter")
```
