# -*- coding: utf-8 -*-
"""
Day 18 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from time import perf_counter

from numpy import zeros

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# PART ONE: COMPLICATED SOLUTION (AND SLOW!)
def Fill(A):
    m, n = A.shape
    for i in range(m):
        f = False
        for j in range(1, n - 1):
            if f: 
                if A[i, j] == 0:
                    A[i, j] = 2
            if A[i, j-1] == 1 and A[i, j] == 2 and f == False:
                f = True
            elif A[i, j-1] == 2 and A[i, j] == 1 and f == True:
                f = False

def PartOne(Ms):
    r, c = 0, 0
    rmin, rmax = +1000, -1000    
    cmin, cmax = +1000, -1000    
    for move, rep in Ms:
        if move == 'U':
            r -= rep
        if move == 'R':
            c += rep
        if move == 'D':
            r += rep
        if move == 'L':
            c -= rep

        rmin, rmax = min(rmin, r), max(rmax, r)
        cmin, cmax = min(cmin, c), max(cmax, c)

    m, n = rmax-rmin, cmax-cmin
    A = zeros( (m+1 , n+1) )
    r, c = -rmin, -cmin

    move0 = None
    for move, rep in Ms:
        if move == 'U':
            A[r-rep:r, c] = 1
            if c+1 < n-1:
                for x in range(r-rep, r):
                    if A[x, c+1] == 0:
                        A[x, c+1] = 2
                if move0 == 'R' and r < m-1:
                    if A[r+1, c+1] == 0:
                        A[r+1, c+1] = 2
                    if A[r, c+1] == 0:
                        A[r, c+1] = 2
            r -= rep
        if move == 'R':
            A[r, c:c+rep+1] = 1
            if r < m-1:
                for y in range(c, c+rep+1):
                    if A[r+1, y] == 0:
                        A[r+1, y] = 2
                if move0 == 'D' and c > 1:
                    if A[r+1, c-1] == 0:
                        A[r+1, c-1] = 2
                    if A[r+1, c] == 0:
                        A[r+1, c] = 2
            c += rep
        if move == 'D':
            A[r:r+rep+1, c] = 1
            if c > 0:
                for x in range(r, r+rep+1):
                    if A[x, c-1] == 0:
                        A[x, c-1] = 2
                if move0 == 'L' and c > 0:
                    if A[r-1, c-1] == 0:
                        A[r-1, c-1] = 2
            r += rep
        if move == 'L':
            A[r, c-rep:c] = 1
            if r > 0:
                for y in range(c-rep, c):
                    if A[r-1, y] == 0:
                        A[r-1, y] = 2
                if move0 == 'U' and r < m-1:
                    if A[r-1, c+1] == 0:
                        A[r-1, c+1] = 2
                    if A[r-1, c] == 0:
                        A[r-1, c] = 2

            c -= rep
        move0 = move
    Fill(A)
    colors = ["black", "darkblue", "gold", "red"]  # use hex colors here, if desired.
    plt.imshow(A, cmap=ListedColormap(colors))
    plt.axis('off')
    plt.show()
    return (A>0).sum()

# PART TWO: best solution also for part 1
def MakeListPs(Ls):
    x, y = 0, 0
    Ps = [(x, y)]
    for l in Ls:
        move, delta = l
        if move == 'U':
            x = x + delta
        if move == 'R':
            y = y + delta
        if move == 'D':
            x = x - delta
        if move == 'L':
            y = y - delta
        Ps.append( (x, y) )
    # From here (simple polygon area):
    # https://en.wikipedia.org/wiki/Polygon#Area
    inside = sum((x1*y2 - x2*y1) for (x1, y1), (x2, y2) in zip(Ps[:-1], Ps[1:]))
    border = sum(l[1] for l in Ls)
    return int(inside + border)//2 + 1

def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    for row in fh:
        move, rep, _ = row.replace('\n', '').split(' ')
        rep = int(rep)
        Ls.append( (move, rep) )
    return MakeListPs(Ls)

def ParserTwo(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    H = ['R', 'D', 'L', 'U']
    for row in fh:
        move, rep, hhex = row.replace('\n', '').split(' ')
        hhex = hhex.replace('#','').replace('(', '').replace(')', '')
        move = H[int(hhex[-1])]
        hhex = hhex[:-1]
        rep = int('0x'+hhex, base=16)
        Ls.append( (move, rep) )

    return MakeListPs(Ls)

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

t0 = perf_counter()
print('Part 1:', Parser(args.filename), 'time:', round(perf_counter() - t0, 3))

t0 = perf_counter() 
print('Part 2:', ParserTwo(args.filename), 'time:', round(perf_counter() - t0, 3))
