## What is the result? - Level 2

1. What is the result of each of the following statements? Explain why.

  * `"" == " "` - False \
    The space between double quotations is whitespace sensitive. The left side corresponds to an empty string of no characters   while the right side corresponds to a single whitespace element
    
  * `'two' > 'three'` - True \
    The values being compared here are of a type `string`, so the comparison operator will perform an element-wise comparison of each character in each of the items using their unicode order. For the first element, `'t'` and `'t'` are compared and found to be equal. Next, the second values, `'w'` and `'h'` are compared. And since the unicode value of `'w'` is higher than that of `'h'`, python will halt the comparison there and return the comparison as `True` 
    
    
  * `[] == []`  - True \
    This is a comparison of two empty lists, and since the types are the same and both have no elements, they are equated to be the same
