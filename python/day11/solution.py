# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from numpy import matrix, where

import matplotlib.pyplot as plt

def Dist(a, b, p, q, Rs, Cs, delta=1):
    tr = 0
    for r in Rs:
        if a < r < p or p < r < a:
            tr += delta
    tc = 0
    for c in Cs:
        if b < c < q or q < c < b:
            tc += delta
    return abs(a - p) + abs(b - q) + tr + tc

def Process(A, delta):
    m, n = A.shape

#    # Plot galaxies
#    plt.imshow(A, cmap='binary')
#    plt.show()

    # Expand
    Rs = [i for i in range(m) if A[i, :].sum() < 1]
    Cs = [j for j in range(n) if A[:, j].sum() < 1]

    Xs, Ys = where(A==1)

    Ps = [(a,b) for a,b in zip(Xs, Ys)]
    
    D = {}
    for a, b in Ps:
        D[a,b] = {}

    for a, b in Ps:
        for p, q in Ps[1:]:
            d = Dist(a, b, p, q, Rs, Cs, delta-1)
            D[a,b][p,q] = d
            D[p,q][a,b] = d

    return sum(sum(D[a,b][p,q] for p,q in D[a,b]) for a,b in D)//2

def Parser(filename, F, delta):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    for row in fh:
        line = row.replace('\n','').replace('#','1').replace('.','0')
        line = [int(c) for c in line]
        Ls.append(line)
    return F(matrix(Ls), delta)


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', Parser(args.filename, Process, 2))
# Solution: 9556896

print('Part 2:', Parser(args.filename, Process, 1000000))
# Solution: 685038186836