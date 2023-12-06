# -*- coding: utf-8 -*-
"""
Day 3 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

from numpy import char

# Return True if nearby symbol:
# ..........
# ...123....
# ......$...
def Neighbour(A, i, j, l):
    n, _ = A.shape
    if i > 0:
        for h in range(j-l-1, j+1):
            if A[i-1, h] != '.' and not A[i-1, h].isdigit():
                return True
    if A[i, j-l-1] != '.' and not A[i, j-l-1].isdigit():
        return True
    if A[i, j] != '.' and not A[i, j].isdigit():
        return True
    if i < n-1:
        for h in range(j-l-1, j+1):
            if A[i+1, h] != '.' and not A[i+1, h].isdigit():
                return True
    return False

def Process1(A):
    n, m = A.shape
    tot = 0
    for i in range(n):
        buf = ''
        for j in range(m):
            if A[i,j].isdigit():
                buf = buf + A[i,j]
            else:
                if buf != '':
                    if Neighbour(A, i, j, len(buf)):
                        tot += int(buf)
                buf = ''
    return tot

# Function for second part
# Return True if '*' has two numbers nearby
# ..........
# .123*.....
# .....431...
def NeighbourStar(A, i, j, l):
    n, _ = A.shape
    if i > 0:
        for h in range(j-l-1, j+1):
            if A[i-1, h] == '*':
                return i-1, h
    if A[i, j-l-1] == '*':
        return i, j-l-1
    if A[i, j] == '*':
        return i, j
    if i < n-1:
        for h in range(j-l-1, j+1):
            if A[i+1, h] == '*':
                return i+1, h
    return -1, -1

def Process2(A):
    n, m = A.shape
    S = {}
    for i in range(n):
        buf = ''
        for j in range(m):
            if A[i,j].isdigit():
                buf = buf + A[i,j]
            else:
                if buf != '':
                    a,b = NeighbourStar(A, i, j, len(buf))
                    if a != -1:
                        if (a,b) not in S:
                            S[a,b] = [int(buf)]
                        else:
                            S[a,b].append(int(buf))
                buf = ''

    return sum([S[k][0] * S[k][1] for k in S if len(S[k]) == 2])

# Parse and count (more functional than Day 1)
def ParseGear(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    # Remark: to simplify the check, add a padding of '.' around the image
    header = fh.readline().replace('\n','')
    n = len(header)+2
    Ls = [['.' for _ in range(n)]]
    Ls.append(['.'] + [c for c in header] + ['.'])
    for r in fh:
        Ls.append(['.'] + [c for c in r.replace('\n','')] + ['.'])
    Ls.append(['.'] + [c for c in header] + ['.'])
    # Instead of using a numpy.matrix of str,
    # just use a numpy.char.array (more memory friendly)
    return F(char.array(Ls))

# Check for PartOne
print('Solution 1:', ParseGear('input.txt', Process1))

# Part 1
# Too low: 536884
# Correct: 537732

# Check for PartTwo
print('Solution 2:', ParseGear('input.txt', Process2))
# Correct: 84883664