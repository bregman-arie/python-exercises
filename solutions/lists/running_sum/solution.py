#!/usr/bin/env python
from typing import List

def running_sum(nums_li: List[int]) -> List[int]:
    """Returns the running sum of a given list of numbers
    
    Args:
        nums_li (list): a list of numbers.

    Returns:
       list: The running sum list of the given list
             [1, 5, 6, 2] would return [1, 6, 12, 14]

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    for i in range(1, len(nums_li)):
        nums_li[i] += nums_li[i - 1]
    return nums_li

if __name__ == '__main__':
    nums_str = input("Insert numbers (e.g. 1 5 1 6): ")
    nums_li = [int(i) for i in nums_str.split()]
    print(running_sum(list(nums_li)))
