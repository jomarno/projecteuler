#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 3
LARGEST PRIME FACTOR

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def largestPrimeFactor(n):
    if n%2==0:
        while n%2==0:
            n = n//2
    
    k = 3
    while k*k <= n:
        if n%k == 0:
            while n%k == 0:
                n=n//k
        k += 2
    
    return n


print(largestPrimeFactor(600851475143))
