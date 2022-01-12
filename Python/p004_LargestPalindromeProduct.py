#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 4
LARGEST PALINDROME PRODUCT

https://projecteuler.net/problem=4


A palindromic number reads the same both ways. The largest palindrome made from 
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def ispalindrome(num):
    digits = str(num)
    return digits == digits[-1::-1]


upperlim = 999
lowerlim = 99

largest = 0
for i in range(upperlim, lowerlim, -1):
    for j in range(upperlim, i-1, -1):
        prod = i*j        
        if prod > largest:
            if ispalindrome(prod):
                largest = prod
        else:
            break

print(largest)

