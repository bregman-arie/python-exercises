#!/usr/bin/env python
# coding=utf-8

def swap_case(s):
    string = ""
    for c in s:
        if c == c.upper():
            string += c.lower()
        else:
            string += c.upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
