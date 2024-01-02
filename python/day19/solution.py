# -*- coding: utf-8 -*-
"""
Day 19 of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

import argparse
from time import perf_counter

import networkx as nx
from collections import namedtuple

Parts = namedtuple('Parts', ['x', 'm', 'a', 's'])
Rule = namedtuple('Rule', ['var', 'bit', 'rhs'])

class Foo(object):
    def __init__(self, a, b, c, d):
        self.x = a
        self.m = b
        self.a = c
        self.s = d
    def __str__(self):
        return "x: {}, m: {}, a: {}, s: {}".format(self.x, self.m, self.a, self.s)

def ParseRules(fh):
    Rules = {}
    for row in fh:
        if len(row) <= 1:
            break
        row = row.replace('}\n','').split('{')
        part = row[0]
        rules = row[1].split(',')
        Rules[part] = []
        for rule in rules:
            if ':' not in rule:
                Rules[part].append( (None, rule) )
            else:
                t, dest = rule.split(':')
                r = Rule(t[0], Sign(t[1]), int(t[2:]))
                Rules[part].append((r, dest ))
    return Rules

def ParseParts(fh):
    Ps = []
    for row in fh:
        row = row.replace('\n', '').replace('{', '').replace('}', '')
        row = row.split(',')
        Ps.append(Parts(int(row[0][2:]), int(row[1][2:]), int(row[2][2:]), int(row[3][2:])))
    return Ps

def Sign(c):
    if c == '>':
        return 1
    return -1

def ProcessPart(Rules, part, flow='in'):
    for rule in Rules[flow]:
        if rule[0] == None:
            if rule[1] == 'A':
                return part.x + part.m + part.a + part.s
            if rule[1] == 'R':
                return 0
            return ProcessPart(Rules, part, rule[1])

        s = rule[0][1]
        if s * getattr(part, rule[0][0]) > s * rule[0][2]:
            if rule[1] == 'A':
                return part.x + part.m + part.a + part.s
            if rule[1] == 'R':
                return 0
            return ProcessPart(Rules, part, rule[1])

def Parser(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    Rules = ParseRules(fh)
    Ps = ParseParts(fh)
    return sum(ProcessPart(Rules, part, 'in') for part in Ps)

def GraphPart(Rules):
    G = nx.DiGraph()

    M = {}
    for rule in Rules:
        M[rule] = {}
        L = []
        for r in Rules[rule]:
            print('rule', rule, r)
            L.append(r[0])
            M[rule][r[1]] = L[:]
            G.add_edge(rule, r[1], length=0)
    
    tot = 0
    for path in nx.all_shortest_paths(G, 'in', 'R', weight='length'):
        Lp = Foo(1, 1, 1, 1)
        Up = Foo(4000, 4000, 4000, 4000)
        for i, j in zip(path[:-1], path[1:]):
            n = len(M[i][j])
            for i, r in enumerate(M[i][j]):
                if r != None:
                    bit = r.bit
                    y = 1
                    if i < n-1:
                        y = 0
                        bit *= -1
                    if bit == 1:
                        v = getattr(Lp, r.var)
                        setattr(Lp, r.var, max(v, r.rhs+y))
                    else:
                        v = getattr(Up, r.var)
                        setattr(Up, r.var, min(v, r.rhs-y))
        tt = (Up.x - Lp.x + 1)*(Up.m - Lp.m + 1)*(Up.a - Lp.a + 1)*(Up.s - Lp.s + 1)
        tot += tt 
        print(path)
        print(Lp)
        print(Up)
        print(tt)

    # for path in nx.all_shortest_paths(G, 'in', 'R', weight='length'):
    #     Lp = Foo(1, 1, 1, 1)
    #     Up = Foo(4000, 4000, 4000, 4000)
    #     for i, j in zip(path[:-1], path[1:]):
    #         n = len(M[i][j])
    #         for i, r in enumerate(M[i][j]):
    #             if r != None:
    #                 bit = r.bit
    #                 y = 1
    #                 if i < n-1:
    #                     y = 0
    #                     bit *= -1
    #                 if bit == 1:
    #                     v = getattr(Lp, r.var)
    #                     setattr(Lp, r.var, max(v, r.rhs+y))
    #                 else:
    #                     v = getattr(Up, r.var)
    #                     setattr(Up, r.var, min(v, r.rhs-y))
    #     tt = (Up.x - Lp.x + 1)*(Up.m - Lp.m + 1)*(Up.a - Lp.a + 1)*(Up.s - Lp.s + 1)
    #     tot += tt 
    #     print(path)
    #     print(Lp)
    #     print(Up)
    #     print(tt)

    return 4000*4000*4000*4000 - tot

#    return 4000*4000*4000*4000 - tot
# 140735544552939
# 140859909617600
# 167409079868000

def ParserTwo(filename):
    fh = open(filename, mode='r', encoding='utf-8')
    return GraphPart(ParseRules(fh))

# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

#t0 = perf_counter() 
#print('Part 1:', Parser(args.filename), 'time:', round(perf_counter() - t0, 3))
# Solution: 
# Too low: 417920


t0 = perf_counter() 
print('Part 2:', ParserTwo(args.filename), 'time:', round(perf_counter() - t0, 3))
# Solution: 