#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))
print('---')
print(makeChange([1256, 54, 48, 16, 102], 1453))
print('---')
print(makeChange([1, 2, 3, 4, 25], 100))
print('---')
print(makeChange([1, 2, 3, 4, 25], 76))
print('---')
print(makeChange([1, 2, 3, 4, 25], 101))
print('---')
print(makeChange([1, 2, 3, 4, 25], 105))

