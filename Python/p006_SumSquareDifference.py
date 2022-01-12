#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 6
SUM SQUARE DIFFERENCE

https://projecteuler.net/problem=6


The sum of the squares of the first ten natural numbers is,

    1² + 2² + ... . 10² = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)² = 55² = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is
    
    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.
"""


def triangular(n):
    """Return the nth triangular number:
    T(n) = 1 + 2 + 3 + ... + n
    """
    return n*(n+1)//2

def pyramidal(n):
    """Return the nth pyramidal number:
    P(n) = 1 + 4 + 9 + ... + n**2
    """
    return triangular(n)*(2*n+1)//3

def sumSquareDiff(n):
    """Return the square of the sum minus the sum of the squares
    """
    return triangular(n)**2 - pyramidal(n)


print(sumSquareDiff(100))

