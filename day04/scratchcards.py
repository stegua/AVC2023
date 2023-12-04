# -*- coding: utf-8 -*-
"""
Day 4 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
def ParseRow(row):
    h, cs = row.split(':')
    play, hand = cs.split('|')
    play = set(int(s) for s in play.split(' ') if s!= '')
    e = 0
    tot = 0
    for h in hand.split(' '):
        if h != '':
            h = int(h)
            if h in play:
                tot = 2**e
                e += 1
    return tot, e

def Parser(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    return sum(F(row)[0] for row in fh)

def ParserTwo(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = [F(row) for row in fh]
    n = len(Ls)
    As = [1 for _ in Ls]
    for i, (_,b) in enumerate(Ls):
        for j in range(i+1, min(n, i+b+1)):
            As[j] += As[i]
    return sum(As)

# Check for PartOne
print('Solution 1:', Parser('input.txt', ParseRow))
# Solution 1: 25231

# Check for PartTwo
print('Solution 2:', ParserTwo('input.txt', ParseRow))
# Solution 2: 9721255
