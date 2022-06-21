## Reverse a file

Reverse an entire file. For example:

```
The
Content
of
a
File
```

The result would be:

```
File
a
of
Content
The
```

### Solution

```python
filename = "reverse_files.txt"
with open(filename) as f:
    lines = f.readlines()
    for line in reversed(lines):
        print(line.strip())
f.close()
```