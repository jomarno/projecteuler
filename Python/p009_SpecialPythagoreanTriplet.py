#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 9
SPECIAL PYTHAGOREAN TRIPLET

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


p = 1000 # Perimeter

# Given p, the upper bound of a is p/(2+sqrt(2)) ~= 0.293p
# It would be a right triangle of equal sides a, b=a

for a in range(1, 1 + int(p*0.293)):

    # Given a and p, then b = p - p^2/(2(p-a))
    # Since p is an integer, b, and therefore c as well, will be integers
    # iff p^2/(2(p-a)) is also an integer
    
    if (p*p) % (2*(p-a)) == 0:

        b = p - p*p//(2*(p-a))
        c = p - a - b
        
        print(a*b*c)
        
        break
