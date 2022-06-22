## Types

1. How to check the type of a variable in Python?
2. How to check if a variable points to an object of an integer type?
3. How to check type of a literal?
4. What `is` operator is used for?
5. if `x = "str"`, what would be the result of `x is str`?

### Solution

1. `type(some_var)`
2. `isinstance(some_var, int)`
3. Same way: `type(2017)` and `isinstance(2022, int)`
4. `is` operator is used to check if two variables/values are located on the same memory area
5. `False` since it checks if x and str type are on the same memory area and it's not)
