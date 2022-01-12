#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 67
MAXIMUM PATH SUM II

https://projecteuler.net/problem=67


By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

        3
       7 4
      2 4 6
     8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 
'Save Link/Target As...'), a 15K text file containing a triangle with 
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible 
to try every route to solve this problem, as there are 299 altogether! If you 
could check one trillion (1012) routes every second it would take over twenty 
billion years to check them all. There is an efficient algorithm to solve it. 
;o)
"""

tree = []
with open('p067_triangle.txt') as fp:
    for line in fp:
        row = [int(number) for number in line.split()]
        tree.append(row)

maxsums = [0]+ tree[0] +[0]
for row in tree[1:]:
    maxsums = [0]+ [ max(num+left, num+right) for num, left, right in zip(row, maxsums[1:], maxsums[:-1]) ] +[0]

print(max(maxsums))
