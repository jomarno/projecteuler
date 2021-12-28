#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 5
SMALLEST MULTIPLE

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isprime(n):
    a = trial_division(n)
    if len(a)==1:
        return True
    else:
        return False

def trial_division(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n = n//2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n = n//f
        else:
            f += 2
    if n != 1: a.append(n)
    # Only odd number is possible
    return a

n = 20

primelist = []
for i in range(1,n+1):
    if isprime(i):
        primelist.append(i)

factorcount = [0]*len(primelist)
for i in range(1,n+1):
    a = trial_division(i)
    for j in range(len(primelist)):
        factorcount[j] = max(factorcount[j],a.count(primelist[j]))

ans = 1
for i in range(len(primelist)):
    ans *=primelist[i]**factorcount[i]

print(ans)
