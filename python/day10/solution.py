# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from numpy import matrix, zeros, where
import matplotlib.pyplot as plt

A = '|-LJ7F.S'
M = {c: i for i, c in enumerate(A)}

# States:
# 0 -> south, north
# 1 -> west,  east
# 2 -> north, south
# 3 -> east,  west

# Map (position, state, action) -> (position, state)
#              0   1   2   3   4   5   6   7
#              |   -   L   J   7   F   5   S
C = matrix([[  0,  0,  0,  0, -1, +1,  0,  2],
            [  0, +1,  0,  0,  0,  0,  0,  2],
            [  0,  0, +1, -1,  0,  0,  0,  2],
            [  0, -1,  0,  0,  0,  0,  0,  2]])

R = matrix([[ -1,  0,  0,  0,  0,  0,  0,  2],
            [  0,  0,  0, -1, +1,  0,  0,  2],
            [ +1,  0,  0,  0,  0,  0,  0,  2],
            [  0,  0, -1,  0,  0, +1,  0,  2]])

# From state to state
S = matrix([[  0,  9,  9,  9,  3,  1,  9, -1],
            [  9,  1,  9,  0,  2,  9,  9, -1],
            [  2,  9,  1,  3,  9,  9,  9, -1],
            [  9,  3,  0,  9,  9,  2,  9, -1]])

def Explore(B, r, c, state):
    n, m = B.shape
    l = 1
    while True:
        action = B[r, c]
        r, c, state = r + R[state, action], c + C[state, action], S[state, action]  
        l += 1 
        if A[B[r, c]] == 'S':
            print('OK', l // 2)
            return l//2
        if state == 9:
            print('FAILED')
            return 2*n*m

def Process(B):
    m, n = B.shape
    r, c = where(B == 7)
    r, c = r[0], c[0]
    # Four cases
    Ls = []
    if r > 0 and B[r-1, c] < 6:   # go north
        Ls.append(Explore(B, r-1, c, 0))
    if r < m-1 and B[r+1, c] < 6: # go south
        Ls.append(Explore(B, r+1, c, 2))
    if c > 0 and B[r, c-1] < 6:   # go west
         Ls.append(Explore(B, r, c-1, 3))
    if c < n-1 and B[r, c+1] < 6:  # go east
         Ls.append(Explore(B, r, c+1, 1))

    return min(Ls)


def ExploreTwo(B, r, c, state):
    n, m = B.shape
    V = zeros( (n, m) )
    V[r, c] = 1
    l = 1
    while True:
        action = B[r, c]
        r, c, state = r + R[state, action], c + C[state, action], S[state, action]  
        V[r, c] = 1
        l += 1 
        if A[B[r, c]] == 'S':
            V[r, c] = 10
            print('OK', l // 2)
            plt.imshow(V)
            plt.show()
            return l//2
        if state == 9:
            print('FAILED')
            return 2*n*m

def ProcessTwo(B):
    m, n = B.shape
    r, c = where(B == 7)
    r, c = r[0], c[0]
    # Four cases
    Ls = []
    if r > 0 and B[r-1, c] < 6:   # go north
        Ls.append(ExploreTwo(B, r-1, c, 0))
    if r < m-1 and B[r+1, c] < 6: # go south
        Ls.append(ExploreTwo(B, r+1, c, 2))
    if c > 0 and B[r, c-1] < 6:   # go west
         Ls.append(ExploreTwo(B, r, c-1, 3))
    if c < n-1 and B[r, c+1] < 6:  # go east
         Ls.append(ExploreTwo(B, r, c+1, 1))

    return min(Ls)


def ParserOne(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    B = matrix([[M[c] for c in row.replace('\n','')] for row in fh])
    return Process(B)

def ParserTwo(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    B = matrix([[M[c] for c in row.replace('\n','')] for row in fh])
    return ProcessTwo(B)



# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

#print('Part 1:', ParserOne(args.filename))
# Solution: 

print('Part 2:', ParserTwo(args.filename))
# Solution: 