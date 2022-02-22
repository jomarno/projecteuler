#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 36
DOUBLE-BASE PALINDROMES

https://projecteuler.net/problem=36


The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
leading zeros.)
"""


def ispalindrome10(num):
    digits = str(num)
    return digits == digits[-1::-1]

def ispalindrome2(num):
    bin_digits = '{0:b}'.format(num)
    return bin_digits == bin_digits[-1::-1]


s = 0
for num in range(1000000):
    if ispalindrome10(num) and ispalindrome2(num):
        s += num

print(s)
