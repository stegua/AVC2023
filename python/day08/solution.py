# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from math import lcm

# Example of input:
# .....

def ProcessOne(cmd, C):
    next = 'AAA'
    idx = 1
    while True:
        for c in cmd:
            next = C[next][c]
            if next == 'ZZZ':
                return idx
            idx += 1

# Look for cycles (and then use periodic conditions)
def CycleNode(node, cmd, C):
    cur = node
    idx = 1
    visited = {}
    while True:
        for c in cmd:
            cur = C[cur][c]
            idx += 1
        if cur in visited:
            return idx-visited[cur]
        visited[cur] = idx

def ProcessTwo(cmd, C):
    nexts = [node for node in C if node[-1] == 'A']
    Next = [CycleNode(node, cmd, C) for node in nexts]
    return lcm(*Next)

def Parser(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    cmd = fh.readline().replace('\n','')
    fh.readline() # empty line
    C = {}
    for row in fh:
        line = row.replace('\n','').replace('= ','')
        for c in '(,)':
            line = line.replace(c, '')
        line = line.split(' ')
        C[line[0]] = {'L': line[1], 'R': line[2]}
    return F(cmd, C)



# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', Parser(args.filename, ProcessOne))
# Solution: 20777

print('Part 2:', Parser(args.filename, ProcessTwo))
# Solution: 13289612809129
