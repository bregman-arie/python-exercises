#!/usr/bin/env python
# coding=utf-8

def remove_duplicates(self, nums: List[int]) -> int:
    l = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[l] = nums[i]
            l += 1
        return l
