## Palindrome

1. Write code that determines if a number is a Palindrome

## Solution

1.

```
from typing import Union

def isNumberPalindrome(number: Union[int, str]) -> bool:
    if isinstance(number, int):
        number = str(number)
    return number == number[::-1]

print(isNumberPalindrome("12321"))
```

- Using Python3.10 that accepts using bitwise operator '|'.

```
def isNumberPalindrome(number: int | str) -> bool:
    if isinstance(number, int):
        number = str(number)
    return number == number[::-1]

print(isNumberPalindrome("12321"))
```

Note: Using slicing to reverse a list could be slower than other options like `reversed` that return an iterator.
