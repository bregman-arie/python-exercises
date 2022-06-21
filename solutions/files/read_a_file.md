## Read a File

Write a code that will read a file and print all its content

### Solution

```python
filename = "python-exercises.txt"

with open(filename) as f:
    content = f.read()
    print(content)
```