#!/usr/bin/env python
# coding=utf-8

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # remove duplicates
    arr = list(dict.fromkeys(arr))
    # sort
    arr.sort()

    print(arr[-2])
