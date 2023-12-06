# -*- coding: utf-8 -*-
"""
Day 2 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

from functools import reduce  

# Build a dictionary with minimal number of cubes
def ParseRow(line):
    ID, game = line.split(':')
    _, ID = ID.split(' ')

    Ds = {}
    for turn in game.split(';'):
        for s in turn.split(','):
            a,b = s.strip().split(' ')
            Ds[b] = max(int(a), Ds.get(b, 0))

    return int(ID), Ds

# Check for infeasibility
def PartOne(line, check):
    id, Ds = ParseRow(line)
    for key in check:
        if Ds.get(key, 0) > check[key]:
            return 0
    return id

# Power of cubes for each row
def PartTwo(line, check=None):
    id, Ds = ParseRow(line)
    return reduce(lambda x,y: x*y, Ds.values(), 1)

# Parse and count (more functional than Day 1)
def ParseCubes(filename, F, Check=None):
    fh = open(filename, mode='r', encoding='utf-8')
    return sum(map(lambda x: F(x.replace('\n',''), Check), fh))

# Check for PartOne
Check = {'red': 12, 'green': 13, 'blue': 14}
print('Solution 1:', ParseCubes('input.txt', PartOne, Check))

# Check for PartTwo
print('Solution 2:', ParseCubes('input.txt', PartTwo))
