#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 14
LONGEST COLLATZ SEQUENCE

The following iterative sequence is defined for the set of positive integers:

      n -> n/2 (n is even)
      n -> 3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

      13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go over one million
"""


from functools import cache

@cache
def collatz_len(a):
    if a == 1:
        return 0
    elif a%2 == 0:
        return 1 + collatz_len(a//2)
    else:
        return 2 + collatz_len((3*a + 1)//2)


lim = 1000000

maxlength = 0

for start in range(2,lim):
    
    length = collatz_len(start)
    
    if length > maxlength:
        maxlength = length
        longest = start

print('Starting term: ', longest)
print('Chain length: ', maxlength)

