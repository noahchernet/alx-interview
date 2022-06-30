#!/usr/bin/python3
'''
Module 0-minoperations.py
Contains function minOperations(n)
'''


def minOperations(n):
    '''
    Calculates the fewest number of operations needed to result in exactly `n`
    number of `H` characters in a file.
    '''
    ans = 0
    d = 2
    while n > 1:
        while n % d == 0:
            ans += d
            n /= d
        d += 1
    return ans
