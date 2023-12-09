# -*- coding: utf-8 -*-
"""
Day 09 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse

def ProcessOne(Ls):
    Rs = []
    for i in range(1, len(Ls)):
        Rs = [Ls[i] - Ls[i-1]] + Rs
        for j in range(1, len(Rs)):
            Rs[j] = Rs[j-1] - Rs[j]
    return Ls[-1] + sum(Rs)        

def ProcessTwo(Ls):
    Rs = []
    Zs = [Ls[0]]
    for i in range(1, len(Ls)):
        Rs = [Ls[i] - Ls[i-1]] + Rs
        for j in range(1, len(Rs)):
            Rs[j] = Rs[j-1] - Rs[j]
        Zs.append(Rs[-1])
    Zs = list(reversed(Zs[:-1]))
    c = 0
    for z in Zs[1:]:
        c = z - c
    return c        

def ParserOne(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    for row in fh:
        line = list(map(int, row.replace('\n','').split(' ')))
        Ls.append(F(line))
    return sum(Ls)


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

#print(ProcessRow(list(map(int, '1 3 6 10 15 21'.split(' ')))))
#print(ProcessRow(list(map(int, '10 13 16 21 30 45'.split(' ')))))

print('Part 1:', ParserOne(args.filename, ProcessOne))
# Solution: 2043677056

print('Part 2:', ParserOne(args.filename, ProcessTwo))
# Solution: 1062

