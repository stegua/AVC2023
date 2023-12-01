# -*- coding: utf-8 -*-
"""
Day 1 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

# Digit and reverse digits in words
# (for reverse string: https://www.digitalocean.com/community/tutorials/python-reverse-string)
FW = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
RW = [w[::-1] for w in FW]
LW = [len(w) for w in FW]

# First digit from the begging
def Forward(line, W, L):
    for i, c in enumerate(line):
        if c.isdigit():
            return c
        for j, w in enumerate(W):
            if line[i:i+L[j]] == w:
                return str(j+1)

    raise Exception('no digit in line:', line)

# Parse and count
def Trebouchet(filename):
    fh = open(filename, mode='r', encoding='utf-8')

    tot = 0
    for row in fh:
        a = Forward(row, FW, LW)
        b = Forward(row[::-1], RW, LW) # reverse line
        
        tot += int(a+b)

    return tot

print('Trebouchet:', Trebouchet('input.txt'))

# My trial for the second part:
# first, too high: 55688
# second, too low: 55352
# finally, correct: 55686