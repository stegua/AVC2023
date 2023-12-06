# -*- coding: utf-8 -*-
"""
Day 5 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

from numpy import zeros, arange
import numpy as np

from time import perf_counter

def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    header = fh.readline()
    t1_start = perf_counter() 

    Seed = [np.int64(c) for c in header.split(':')[1].strip().split(' ')]
    Ps = [(Seed[i], Seed[i+1]) for i in range(0, len(Seed), 2)]
    tlen = 0
    for a,b in Ps:
        tlen += b
    Seed = zeros(tlen, dtype=np.int64)
    Rs = []
    idx = 0
    for a,b in Ps:
        Seed[idx:idx+b] = arange(a, a+b, dtype=np.int64)
        Rs.append( (idx, a, b) )
        idx += b
    Ps = Rs
    t1_stop = perf_counter()
    print("Elapsed time:", t1_stop - t1_start)
    fh.readline()
    s = ''
    for row in fh:
        if row == '\n':
            Hs = s.split('\n')
            S0 = np.copy(Seed)
            mmin, mmax = Seed.min(), Seed.max()
            for buf in Hs[1:-1]:
                if buf != '':
                    dest, source, ra = list(map(np.int64, buf.split(' ')))
                    delta = dest-source
                    for idx, a, b in Rs:
                        if mmax < a or mmin > a+b:
                            pass
                        else: 
                            S0[idx:idx+b] = np.where((Seed[idx:idx+b] >= source) & (Seed[idx:idx+b] < source + ra),
                                                   Seed[idx:idx+b] + delta, S0[idx:idx+b]) 

            Seed = np.copy(S0)
            print(S0)
            s = ''
            t1_stop = perf_counter()
            print("Elapsed time:", Hs[0], round(t1_stop - t1_start, 3))
        else:
            s = s + row
    if s != '':
        Hs = s.split('\n')
        S0 = np.copy(Seed)
        mmin, mmax = Seed.min(), Seed.max()
        for buf in Hs[1:-1]:
            if buf:
                dest, source, ra = list(map(np.int64, buf.split(' ')))
                delta = dest-source
                for idx, a, b in Rs:
                    if mmax < a or mmin > a+b:
                        pass
                    else: 
                        S0[idx:idx+b] = np.where((Seed[idx:idx+b] >= source) & (Seed[idx:idx+b] < source + ra),
                                                   Seed[idx:idx+b] + delta, S0[idx:idx+b]) 
    t1_stop = perf_counter()
    print("Elapsed time:", round(t1_stop - t1_start, 3))
    print(S0)
    return S0.min()


# Check for PartOne (Lost!)
#print('Solution 1:', Parser('input.txt'))

# Check for PartTwo
print('Solution 2:', Parser('small.txt'))
