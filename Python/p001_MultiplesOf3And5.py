#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 1
MULTIPLES OF 3 AND 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multsum(num, lim):
    """Returns the sum of all multiples of num below lim"""
    
    # Let n be the number of multiples of num below lim
    # The sum of the multiples is equal to num times the nth triangular number
    # 1*num + 2*num + ... + n*num = num*(1 + 2 + ... + n) = num*n*(n+1)/2

    n = lim//num
    return num*n*(n+1)//2


lim = 1000

# Add multiples of 3 and multiples of 5
# Substract numbers counted twice (multiples of both)
print(multsum(3,lim) + multsum(5,lim) - multsum(3*5,lim))
