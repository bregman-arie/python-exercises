## Break Out

Write a loop that will keep reversing user's input until he enters the letter 'q' to quit

## Solution

```python
while True:
  ans = input("Please insert a string to reverse: ")
  if ans == 'q':
      break
  print(ans[::-1])
```
