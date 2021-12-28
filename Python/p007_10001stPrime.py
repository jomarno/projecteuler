#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 7
10001ST PRIME

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


from math import sqrt

def isprime(n):
    if n > 3:
        if n%2==0 or n%3==0: return False
        
        for k in range(5, int(sqrt(n))+1, 6):
            if n%k==0 or n%(k+2)==0: return False

        return True
    else: return n > 1

def nthprime(n):
    primecount = 0
    num = 0
    
    while primecount < n:
        num += 1

        if isprime(num):
            primecount += 1
    
    return num


print(nthprime(10001))

