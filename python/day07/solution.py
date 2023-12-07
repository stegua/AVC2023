# -*- coding: utf-8 -*-
"""
Day 7 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse

# SOLUTION PART 1
# Card values
RANK = 'AKQJT98765432'  # 13 carte
KNAR = [i+1 for i,_ in enumerate(RANK)]
VALUE = {c: i for c, i in zip(RANK, KNAR)}

def HandType(hand):
    D = {}
    # Count cards
    for c in hand:
        D[c] = D.get(c, 0) + 1

    if len(D) == 1: # AAAAA
        return 1
    if len(D) == 2: 
        if min(D[k] for k in D) == 1: # AA8AA
            return 2
        return 3 # 23332
    if len(D) == 3:
        if max(D[k] for k in D) == 3: # TTT98
            return 4
        return 5 # 23432
    if len(D) == 4:
        return 6 # A23A4
    if len(D) == 5:
        return 7 # 23456
    raise RuntimeError

def HandMap(hand):
    return (HandType(hand), tuple(VALUE[c] for c in hand))

def ParserOne(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    for row in fh:
        hand = row.replace('\n','').split(' ')
        a, b = hand[0], int(hand[1])
        Ls.append( (a, b) )
    Ls.sort(key=lambda x: HandMap(x[0]), reverse=True)
    return sum((i+1)*hand[1] for i, hand in enumerate(Ls))

# SOLUTION PART 2
def HandType2(hand):
    D = {}
    # Count cards
    jolly = 0
    for c in hand:
        if c == 'J':
            jolly += 1
        else:
            D[c] = D.get(c, 0) + 1

    if len(D) == 0:
        cmax = 5
    else:
        cmax = max(D[k] for k in D if k != 'J') + jolly
        cmin = min(D[k] for k in D if k != 'J')

    if cmax == 5: # AAAAA AAJAA
        return 1
    if cmax == 4: # AA8AA AA8JA
        return 2
    if cmax == 3: # 23331 23332 # 23J32 # 23J31
        if cmin == 2:
            return 3
        return 4 
    if cmax == 2:
        if len(D) == 3:
            return 5
        return 6 # A23A4 # 23432
    if cmax == 1:
        return 7 # 23456
    raise RuntimeError

def HandMap2(hand):
    return (HandType2(hand), tuple(VALUE[c] for c in hand))

def ParserTwo(filename):
    global RANK
    RANK = 'AKQT98765432J'  # J is in last position

    fh = open(filename, mode='r', encoding='utf-8')
    Ls = []
    for row in fh:
        hand = row.replace('\n','').split(' ')
        a, b = hand[0], int(hand[1])
        Ls.append( (a, b) )
    Ls.sort(key=lambda x: HandMap2(x[0]), reverse=True)
    return sum((i+1)*hand[1] for i, hand in enumerate(Ls))


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

print('Part 1:', ParserOne(args.filename))
# Solution: it should be 6440
#Too low: 247651230

print('Part 2:', ParserTwo(args.filename))
# Solution: 
# To high: 249959407
