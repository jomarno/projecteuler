#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 72
COUNTING FRACTIONS

https://projecteuler.net/problem=72


Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

import numpy as np

def trial_division(n):
    """Takes an integer n and returns a list of its prime factors
    """
    factor_list = []
    while n % 2 == 0:
        factor_list.append(2)
        n = n//2
    f = 3
    while f*f <= n:
        if n % f == 0:
            factor_list.append(f)
            n = n//f
        else:
            f += 2
    if n != 1: factor_list.append(n)
    # Only odd number is possible
    return factor_list

def phi(n):
    """Calculates Euler's totient function
    """
    factor_list = trial_division(n)
    factors, counts = np.unique(np.array(factor_list), return_counts=True)

    result = 1
    for p, k in zip(factors, counts):
        result *= (p-1)*p**(k-1)

    return result

n = 1000000
length = 0
for i in range(2, n+1):
    length += phi(i)

print(length)