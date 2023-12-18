# -*- coding: utf-8 -*-
"""
Day 18 of Advent of Code, December 2023
https://adventofcode.com/


Benchmark on Mac Book Air - M2

% hyperfine --runs 10 'python3 solution.py -f input.txt'
Benchmark 1: python3 solution.py -f input.txt
  Time (mean ± σ):      17.8 ms ±   1.3 ms    [User: 14.1 ms, System: 3.1 ms]
  Range (min … max):    17.1 ms …  21.4 ms    10 runs

@author: gualandi
"""

import argparse
from time import perf_counter

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