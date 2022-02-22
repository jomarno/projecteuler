#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 15
LATTICE PATHS

https://projecteuler.net/problem=15


Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

"""


from math import comb

def latticePaths(n):
    return sum([comb(n,k)**2 for k in range(n+1)])

print(latticePaths(20))
