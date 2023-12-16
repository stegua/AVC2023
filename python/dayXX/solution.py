# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from time import perf_counter

import numpy as np
from numpy import matrix, zeros

def PartOne():
    return 0


def PartTwo():
    return 0


def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    return 0


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

t0 = perf_counter() 
print('Part 1:', Parser(args.filename, PartOne), 'time:', round(perf_counter() - t0, 3))
# Solution: 

#t0 = perf_counter() 
#print('Part 2:', Parser(args.filename, PartTwo), 'time:', round(perf_counter() - t0, 3))
# Solution: 