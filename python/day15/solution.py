# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse

# First part
def HASH(s):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h

def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    return sum(HASH(c) for c in fh.read().replace('\n','').split(','))

# Second part
def Process(Ws):
    B = [{} for _ in range(256)]
    I = {}
    for w in Ws:
        if '-' == w[-1]:
            box = w[:-1]
            nbox = HASH(box)
            if box in B[nbox]:
                del B[nbox][box]
        else:
            box, focal = w.split('=')
            nbox = HASH(box)
            B[nbox][box] = int(focal)
            I[box] = nbox
        
    tot = 0
    for i in range(256):
        if B[i] != {}:
            for j, key in enumerate(B[i]):
                tot += (i+1)*(j+1)*B[i][key]
    return tot

def ParserTwo(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    return Process(fh.read().replace('\n','').split(','))

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', Parser(args.filename))
print('Part 2:', ParserTwo(args.filename))
