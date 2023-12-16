# -*- coding: utf-8 -*-
"""
Day 16 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from time import perf_counter

import numpy as np
from numpy import matrix, zeros

from collections import namedtuple
# Define a nametuple as exercise
Step = namedtuple('Step', ['r', 'c', 'dir'])

# Directions:
D = {'north': (-1, 0), 'south': (+1, 0), 'east': (0, +1), 'west': (0, -1)}

def Next(A, B, r, c, direction):
    m, n = A.shape
    if r < 0 or c < 0 or r >= m or c >= n:
        return []
    
    B[r,c] = 1

    if A[r, c] == 0: # Continue in the same direction
        dx, dy = D[direction]
        return [Step(r + dx , c + dy, direction)]

    if A[r, c] == 1: # Open two directions direction
        if direction == 'north' or direction == 'south':
            dx, dy = D[direction]
            return [Step(r + dx , c + dy, direction)]
        N = []
        for dir in ['north', 'south']:
            dx, dy = D[dir]
            N.append(Step(r + dx, c + dy, dir))
        return N
    
    if A[r, c] == 2: # Open two directions direction
        if direction == 'west' or direction == 'east':
            dx, dy = D[direction]
            return [Step(r + dx , c + dy, direction)]
        N = []
        for dir in ['west', 'east']:
            dx, dy = D[dir]
            N.append(Step(r + dx, c + dy, dir))
        return N
    
    # A is either 3 or 4
    if direction == 'east' and A[r, c] == 4: # --> / 
        (dx, dy), direct = D['north'], 'north'
    if direction == 'east' and A[r, c] == 3: # --> \
        (dx, dy), direct = D['south'], 'south'

    if direction == 'west' and A[r, c] == 4: # --> / 
        (dx, dy), direct = D['south'], 'south'
    if direction == 'west' and A[r, c] == 3: # --> \
        (dx, dy), direct = D['north'], 'north'

    if direction == 'north' and A[r, c] == 4: # --> / 
        (dx, dy), direct = D['east'], 'east'
    if direction == 'north' and A[r, c] == 3: # --> \
        (dx, dy), direct = D['west'], 'west'

    if direction == 'south' and A[r, c] == 4: # --> / 
        (dx, dy), direct = D['west'], 'west'
    if direction == 'south' and A[r, c] == 3: # --> \
        (dx, dy), direct = D['east'], 'east'

    if dx == 0 and dy == 0:
        raise RuntimeError
    return [Step(r + dx, c + dy, direct)]

def Process(A, B, r, c, dir):
    B[:, :] = 0
    Ps = [Step(r, c, dir)]
    Moves = set()
    while len(Ps) > 0:
        Ns = []
        for p in Ps:
            if p not in Moves:
                Ns.extend(Next(A, B, p.r, p.c, p.dir))
                Moves.add(p)
        Ps = Ns[:]
    return B.sum()


def PartOne(A):
    m, n = A.shape
    B = zeros( (m, n), dtype=int )
    return Process(A, B, 0, 0, 'east')

def PartTwo(A):
    m, n = A.shape
    B = zeros( (m, n), dtype=int )
    Ls = []
    for r in range(m):
        Ls.append( Process(A, B, r, 0,   'east') )
        Ls.append( Process(A, B, r, n-1, 'west') )
    for c in range(n):
        Ls.append( Process(A, B, 0, c,   'south') )
        Ls.append( Process(A, B, m-1, c, 'north') )
    return max(Ls)

def Parser(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    As = []
    for row in fh:
        row = row.replace('\n','').replace('.','0')
        row = row.replace('|', '1').replace('-', '2')
        row = row.replace('\\', '3').replace('/', '4')
        row = list(map(int, row))
        As.append(row)
    return F(matrix(As, dtype=int))


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

t0 = perf_counter() 
print('Part 1:', Parser(args.filename, PartOne), 'time:', round(perf_counter() - t0, 3))
# Solution: 

t0 = perf_counter() 
print('Part 2:', Parser(args.filename, PartTwo), 'time:', round(perf_counter() - t0, 3))
# Solution: 