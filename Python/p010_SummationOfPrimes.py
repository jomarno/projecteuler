#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 10
SUMMATION OF PRIMES

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from math import sqrt

def isprime(n):
    if n > 3:
        if n%2==0 or n%3==0: return False
        for k in range(5, int(sqrt(n))+1, 6):
            if n%k==0 or n%(k+2)==0: return False
        return True
    else: return n > 1

def primesum(lim):
    s = 0
    for num in range(1, lim):
        if isprime(num):
            s += num
    return s

# def primesum(lim):
#     return sum([n for n in range(lim) if isprime(n)])


print(primesum(2000000))

