#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 71
ORDERED FRACTIONS

https://projecteuler.net/problem=71


Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.
"""


# from functools import cache

# @cache
def euclidgcf(m, n):
    """Calculates the greatest common factor using Euclid's algorithm
    """
    if n == 0:
        return m
    else:
        return euclidgcf(n, m % n)

def getn(d, target):
    """Returns the numerator n of the fraction n/d closest (but not equal) to target
    """
    m = d*target.n
    n = m // target.d
    if m % target.d == 0:
        n -= 1
    return n

class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.val = n/d

    def makeProper(self):
        gcf = euclidgcf(n, d)
        self.n //= gcf
        self.d //= gcf
        
target = Fraction(3, 7)
closest = Fraction(1, 1)
smallestDiff = 1
dmax = 1000000
for d in range(2, dmax+1):
    n = getn(d, target)
    test = Fraction(n, d)
    diff = target.val - test.val
    if diff < smallestDiff:
        test.makeProper()
        closest = test
        smallestDiff = diff

print(closest.n)

    

    









        
        


