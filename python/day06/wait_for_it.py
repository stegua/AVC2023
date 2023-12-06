# -*- coding: utf-8 -*-
"""
Day 6 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""


from numpy import zeros, arange
import numpy as np

from time import perf_counter
from math import sqrt, ceil, floor

def SolveEq(t,d):
    # Solve second order equation for v * (v-t) <= d
    # than take care to have only integers v in interval x1 <= v < x2
    a = 1
    b = -t
    c = d
    delta = sqrt(b**2 - 4*a*c)
    x1 = (-b + delta)/(2*a) 
    x2 = (-b - delta)/(2*a) 
    if x2 < x1:
        x1, x2 = x2, x1
    if abs(x2 - int(x2)) < 1e-09:
        x2 = x2 - 1
    else:
        x2 = x2 + 1
    return int(ceil(x1)), int(floor(x2))

# Example of input:
# Time:      7  15   30
# Distance:  9  40  200
def ProcessTime(time, dist):
    tot = 1
    for t, d in zip(time, dist):
        v1, v2 = SolveEq(t, d)
        tot *= v2 - v1
    return tot

def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    time = [int(s) for s in fh.readline().split(':')[1].strip().split(' ') if s!= '']
    dist = [int(s) for s in fh.readline().split(':')[1].strip().split(' ') if s!= '']
    return ProcessTime(time, dist)

def Parser2(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    time = int(fh.readline().split(':')[1].strip().replace(' ',''))
    dist = int(fh.readline().split(':')[1].strip().replace(' ',''))
    return ProcessTime([time], [dist])

print('Part 1:', Parser('./input.txt'))
# Solution: 71503

print('Part 2:', Parser2('./input.txt'))
# Solution: 39132886