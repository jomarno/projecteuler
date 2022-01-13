#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROJECT EULER - PROBLEM 17
NUMBER LETTER COUNTS

https://projecteuler.net/problem=17


If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
letters. The use of "and" when writing out numbers is in compliance with 
British usage.
"""


def letterCount(number):
    """Returns the letter count of any integer between 1 and 999 when written 
    out in words.
    """

    digits = str(number).zfill(3)

    # Letter count of numbers up to 19
    letters1 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]

    # Letter count of tens from 20 to 90
    letters10 = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

    # Units and tens
    if int(digits[-2:]) < 20:
        count = letters1[int(digits[-2:])]
    else:
        count = letters10[int(digits[-2])] + letters1[int(digits[-1])]
    
    # Hundreds
    if digits[-3] != '0':
        count += letters1[int(digits[-3])] + 7
        if digits[-2:] != '00':
            count += 3
    
    return count

letterCountSum = 11 # Letter count of "one thousand", not included in loop
for number in range(1000):
    letterCountSum += letterCount(number)

print(letterCountSum)
