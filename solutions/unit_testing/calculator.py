#!/usr/bin/env python
# coding=utf-8
import unittest

# Function definitions
def add(x, y):
    """Add numbers"""
    return x + y

def subtract(x, y):
    """Subtract numbers"""
    return x - y

def multiply(x, y):
    """Multiply numbers"""
    return x * y

def divide(x, y):
    """Divide numbers"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

# Unit testing
class TestCalculator(unittest.TestCase):

    def test_add(self):
        assert add(1, 2) == 3, "Should be 3"
        assert add(99, 101) == 200, "Should be 200"
        assert add(-10, -50) == -60, "Should be 60"

    def test_subtract(self):
        assert subtract(1, 2) == -1, "Should be -1"
        assert subtract(10, 50) == -40, "Should be -40"
        assert subtract(40, 20) == 20, "Should be 20"

    def test_multiply(self):
        assert multiply(1, 2) == 2, "Should be 2"
        assert multiply(-10, 30) == -300, "Should be 300"
        assert multiply(-4, 0) == 0, "Should be 0"

    def test_divide(self):
        assert divide(1, 2) == 0.5, "Should be 0.5"
        assert divide(200, 40) == 5, "Should be 5"
        # Handle ValueError, 1st method:
        self.assertRaises(ValueError, divide, 1, 0)
        # Handle ValueError, 2nd method:
        with self.assertRaises(ValueError):
            divide(1, 0)

# Perform unittest
unittest.main()
