# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from numpy import matrix, not_equal

def CheckRow(A):
    m, _ = A.shape
    for i in range(m-1):
        d = min(i, m-2-i)
        As = [x for x in range(i-d, i+1)]
        Bs = [x+1 for x in range(i, i+d+1)]
        diff = 0
        for a, b in zip(reversed(As), Bs):
            diff += not_equal(A[a, :], A[b, :]).sum()
        if diff == DELTA:
            return i+1
    return 0

def CheckCol(A):
    _, n = A.shape
    for i in range(n-1):
        d = min(i, n-2-i)
        As = [x for x in range(i-d, i+1)]
        Bs = [x+1 for x in range(i, i+d+1)]
        diff = 0
        for a, b in zip(reversed(As), Bs):
            diff += not_equal(A[:, a], A[:, b]).sum()
        if diff == DELTA:
            return i+1
    return 0

def Process(A):
    a = CheckCol(A)
    if a > 0:
        return a 
    return 100 * CheckRow(A)

def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    Rs = []
    for row in fh:
        row = row.replace('\n','').strip()
        if row == '':
            Rs.append(Process(matrix(Ls)))
            Ls = []
        else:
            row = list(map(lambda z: 0 if z=='.' else 1, row))
            Ls.append(row)
    if Ls != []:
        Rs.append(Process(matrix(Ls))) 
    return sum(Rs)

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

# Part 1: DELTA = 0
# Part 2: DELTA = 1
DELTA = 0
print('Part 1:', Parser(args.filename))

DELTA = 1
print('Part 2:', Parser(args.filename))
