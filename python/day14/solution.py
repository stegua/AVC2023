# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from numpy import matrix
import numpy as np

M = {'O': 1, '.': 2, '#': 0}

def ScanNorth(A):
    m, n = A.shape
    for c in range(n):
        Ls = []
        t = [m, 0, 0]
        for r in range(m):
            v = A[r,c]
            if v == 0:
                t[0] = r
                Ls.append(t)
                t = [m, 0, 0]
            else:
                t[v] += 1
        Ls.append(t)

        idx = 0
        for t in Ls:
            for _ in range(t[1]):
                A[idx, c] = 1  # 'O'
                idx += 1
            for _ in range(t[2]):
                A[idx, c] = 2  #'.'
                idx += 1
            idx += 1

def ScanWest(A):
    m, n = A.shape
    for r in range(m):
        Ls = []
        t = [m, 0, 0]
        for c in range(n):
            v = A[r,c]
            if v == 0:
                t[0] = r
                Ls.append(t)
                t = [m, 0, 0]
            else:
                t[v] += 1
        Ls.append(t)

        idx = 0
        for t in Ls:
            for _ in range(t[1]):
                A[r, idx] = 1  # 'O'
                idx += 1
            for _ in range(t[2]):
                A[r, idx] = 2  #'.'
                idx += 1
            idx += 1

def ScanSouth(A):
    m, n = A.shape
    for c in range(n):
        Ls = []
        t = [m, 0, 0]
        for r in range(m-1, -1, -1):
            v = A[r,c]
            if v == 0:
                t[0] = r
                Ls.append(t)
                t = [m, 0, 0]
            else:
                t[v] += 1
        Ls.append(t)

        idx = m-1
        for t in Ls:
            for _ in range(t[1]):
                A[idx, c] = 1  # 'O'
                idx -= 1
            for _ in range(t[2]):
                A[idx, c] = 2  #'.'
                idx -= 1
            idx -= 1

def ScanEast(A):
    m, n = A.shape
    for r in range(m):
        Ls = []
        t = [m, 0, 0]
        for c in range(n-1, -1, -1):
            v = A[r,c]
            if v == 0:
                t[0] = r
                Ls.append(t)
                t = [m, 0, 0]
            else:
                t[v] += 1
        Ls.append(t)

        idx = n-1
        for t in Ls:
            for _ in range(t[1]):
                A[r, idx] = 1  # 'O'
                idx -= 1
            for _ in range(t[2]):
                A[r, idx] = 2  #'.'
                idx -= 1
            idx -= 1

def ProcessOne(A):
    m, _ = A.shape
    ScanNorth(A)
    A = A == 1
    return sum([(m-i)*v[0] for i,v in enumerate(np.sum(A, axis=1).tolist())])

def Process(A, C = 1000000000):
    m, _ = A.shape
    D = {}
    for i in range(C):
        xx = hash(A.data.tobytes())
        if xx in D:
            if D[xx][1] == 2:
                p = i - D[xx][0]
                stop = C - ((C - D[xx][0])//p)*p - D[xx][0]
                break
            D[xx] = (i, D[xx][1]+1)
        else:
            D[xx] = (i, 1)
        ScanNorth(A)
        ScanWest(A)
        ScanSouth(A)
        ScanEast(A)
    for i in range(stop):
        ScanNorth(A)
        ScanWest(A)
        ScanSouth(A)
        ScanEast(A)

    A = A == 1
            
    return sum([(m-i)*v[0] for i,v in enumerate(np.sum(A, axis=1).tolist())])

def Parser(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    A = [[M[c] for c in row.replace('\n','')] for row in fh]
    return F(matrix(A))

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', Parser(args.filename, ProcessOne))
# Solution: 

print('Part 2:', Parser(args.filename, Process))
# Solution: 