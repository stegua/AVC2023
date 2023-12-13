# -*- coding: utf-8 -*-
"""
Day 12 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from time import perf_counter
from functools import cache

@cache
def Check(s, n):
    if len(s) < n:
        return False    
    for i in range(n):
        if s[i] == '.':
            return False
    if len(s) == n:
        return True
    if s[n] == '.' or s[n] == '?':
        return True
    return False

@cache
def Process(s, Ls, left):
    if len(Ls) == 0:
        if s == '':
            return 1
        if '#' in s:
            return 0
        return 1
    if s == '':
        return 0

    if len(s) < left:
        return 0

    if s[0] == '.':
        return Process(s[1:], Ls, left)
    
    if s[0] == '#':
        n = Ls[0]
        if Check(s, n):
            return Process(s[n+1:], Ls[1:], left-Ls[0]-1)
        return 0 

    if s[0] == '?':
        a = Process(s[1:], Ls, left)
        n = Ls[0]
        b = 0
        if Check(s, n):
            b = Process(s[n+1:], Ls[1:], left-Ls[0]-1)
        return a + b
    
    raise RuntimeError(s)

def Multiply(code, Bs, i):
    c = (code+'?')*i
    return c[:-1], Bs*i

def Parser(filename, alpha):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    for i, l in enumerate(fh):
        #t0_stop = perf_counter()

        r = l.replace('\n','')
        code, bs = r.split(' ')
        Bs = [int(c) for c in bs.split(',')]
        code, Bs = Multiply(code, Bs, alpha)
        Ls.append( Process(code, tuple(Bs), sum(Bs)+len(Bs)-1) )
        
        #t1_stop = perf_counter()
        #print('row:', i+1, '- time:', round(t1_stop - t0_stop, 4))

    return sum(Ls)

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', Parser(args.filename, 1))

print('Part 2:', Parser(args.filename, 5))
