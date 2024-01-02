# -*- coding: utf-8 -*-
"""
Day 21 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from time import perf_counter

from numpy import matrix, zeros

import networkx as nx
from numpy import polyfit

def MakeDigraph(A):
    m, n = A.shape
    # Build the search graph
    G = nx.DiGraph()

    for r in range(m):
        for c in range(n-1):
            if A[r, c] != 1 and A[r, c+1] != 1:
                G.add_edge( (r, c), (r, c+1))
                G.add_edge( (r, c+1), (r, c))

    for r in range(m-1):
        for c in range(n):
            if A[r, c] != 1 and A[r+1, c] != 1:
                G.add_edge( (r, c), (r+1, c))
                G.add_edge( (r+1, c), (r, c))

    return G

def Count(A, G, CUTOFF):
    # Find start position
    m, n = A.shape
    x, y = m//2, n//2

    # Shortest path from origin
    dist = nx.single_source_shortest_path_length(G, (x,y), CUTOFF )

    tot = 0
    MOD = CUTOFF % 2 # 1 per cutoff dispari, 0 per pari
    for v in dist:
        if dist[v] % 2 == MOD:
            tot+= 1

    return tot

def PartOne(B, G, steps=64):
    # Build the search graph
    G = MakeDigraph(B)
    # Count the destinations
    return Count(B, G, steps)


def PartTwo(B, G, s=26501365):
    # 26501365 = 131 * k + 65

    x = [65 + i*131 for i in range(3)]
    y = [Count(B, G, v) for v in x]

    # Fit a polynomial of degree 2
    a, b, c = polyfit(x, y, deg=2)

    return int(round(a*s*s + b*s + c))


def Parser(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    As = []
    for row in fh:
        As.append( [int(c) for c in row.replace('\n', '').replace('.','0').replace('#','1').replace('S','0')] )  

    A = matrix(As)
    m, n = A.shape
    N = 5
    B = zeros( (N*m, N*n) )
    for i in range(N):
        for j in range(N):
            B[i*m:(i+1)*m, j*n:(j+1)*n] = A
    
    G = MakeDigraph(B)

    return F(B, G)

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

t0 = perf_counter() 
print('Part 1:', Parser(args.filename, PartOne), 'time:', round(perf_counter() - t0, 3))

t0 = perf_counter() 
print('Part 2:', Parser(args.filename, PartTwo), 'time:', round(perf_counter() - t0, 3))