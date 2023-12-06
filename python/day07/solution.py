# -*- coding: utf-8 -*-
"""
Day XX of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse

# Example of input:
# .....

def ParserOne(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    print(fh.readline())
    return 0

def ParserTwo(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    print(fh.readline())
    return 0


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', ParserOne(args.filename))
# Solution: 

print('Part 2:', ParserTwo(args.filename))
# Solution: 