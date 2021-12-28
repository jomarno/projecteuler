#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 69
TOTIENT MAXIMUM

Euler's Totient function, φ(n) [sometimes called the phi function], is used to 
determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively 
prime to nine, φ(9)=6.

    n       Relatively Prime    φ(n)    n/φ(n)

    2       1                   1       2
    3       1,2                 2       1.5
    4       1,3                 2       2
    5       1,2,3,4             4       1.25
    6       1,5                 2       3
    7       1,2,3,4,5,6         6       1.1666...
    8       1,3,5,7             4       2
    9       1,2,4,5,7,8         6       1.5
    10      1,3,7,9             4       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""


import numpy as np

def trial_division(n):
    factor_list = []
    while n % 2 == 0:
        factor_list.append(2)
        n = n//2
    f = 3
    while f * f <= n:
        if n % f == 0:
            factor_list.append(f)
            n = n//f
        else:
            f += 2
    if n != 1: factor_list.append(n)
    # Only odd number is possible
    return factor_list

def phi(n):
    factor_list = np.array(trial_division(n))
    factors, counts = np.unique(factor_list, return_counts=True)

    result = 1
    for p, k in zip(factors, counts):
        result *= (p-1)*p**(k-1)

    return result


max_n_over_phi = 0
corresponding_n = 0
for n in range(6, 1000000):
    n_over_phi = n/phi(n)
    if n_over_phi > max_n_over_phi:
        max_n_over_phi = n_over_phi
        corresponding_n = n
        # print(n)

print(corresponding_n)
