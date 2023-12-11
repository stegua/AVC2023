# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from numpy import matrix, zeros, where
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

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

def ParserOne(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    B = matrix([[M[c] for c in row.replace('\n','')] for row in fh])
    return Process(B)


# Part Two : track "internal path"

# States:
# 0 -> south, north
# 1 -> west,  east
# 2 -> north, south
# 3 -> east,  west
# Actions: " |   -   L   J   7   F "
#            0   1   2   3   4   5  
D = {
    (0, 0): [(0, -1)],  # Map (state, action) -> offset (sx going down)
    (2, 0): [(0, +1)],  # Map (state, action) -> offset (dx going up)

    (1, 1): [(-1, 0)],  # Map (state, action) -> offset (sx going down)
    (3, 1): [(+1, 0)],  # Map (state, action) -> offset (dx going up)

    (2, 2): [],                           # north-south, L
    (3, 2): [(0, -1), (+1, -1), (+1, 0)], # east, west,  L

    (2, 3): [(0, +1), (+1, +1), (+1, 0)], # north-south, J
    (1, 3): [],                           # west, east,  J

    (1, 4): [(-1, 0), (-1, +1), (0, +1)], # west-east,   7
    (0, 4): [],                           # south-north, 7

    (0, 5): [(0, -1), (-1, -1), (-1, 0)], # south-north, F
    (3, 5): [],                           # west, east,  F
}

def F(B, r, c, state, V):
    m, n = V.shape
    if (state, B[r,c]) in D:
        for p, q in D[state, B[r,c]]:
            if 0 <= r+p < m and 0 <= c+q < n and V[r+p, c+q] == 0:
                V[r+p, c+q] = 2

def Count(V):
    m, n = V.shape
    tt = 0
    for r in range(m):
        open = False
        for c in range(n):
            if not open and c < n-1 and V[r,c] == 0 and V[r,c+1] == 2:
                return float('inf')
            if open or (V[r,c] == 2 and not open):
                tt += 1
                open = True
            if open and c < n-1 and V[r,c+1] == 1:
                open = False
    return tt

def ExploreTwo(B, r, c, state, plot=True):
    n, m = B.shape
    V = zeros( (n, m) )
    V[r, c] = 1
    F(B, r, c, state, V)
    while True:
        action = B[r, c]
        r, c, state = r + R[state, action], c + C[state, action], S[state, action]  
        V[r, c] = 1
        if A[B[r, c]] == 'S':
            V[r, c] = 3
            if plot:
                colors = ["black", "darkblue", "gold", "red"]  # use hex colors here, if desired.
                plt.imshow(V, cmap=ListedColormap(colors))
                plt.axis('off')
                plt.savefig('dump{}.png'.format(state))
                plt.show()
            return Count(V)
        if state == 9:
            return float('inf')
        F(B, r, c, state, V)

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
# Solution: 433
# Too low: 285