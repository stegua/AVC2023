# -*- coding: utf-8 -*-
"""
Day 17 of Advent of Code, December 2023
https://adventofcode.com/


% hyperfine --runs 10 'python3 solution.py -f input.txt'
Benchmark 1: python3 solution.py -f input.txt
  Time (mean ± σ):      6.730 s ±  0.296 s    [User: 7.608 s, System: 0.970 s]
  Range (min … max):    6.437 s …  7.512 s    10 runs

@author: gualandi
"""

import argparse
from time import perf_counter

import numpy as np
from numpy import matrix, zeros

import networkx as nx

from collections import namedtuple

# SEE Pytohc Docs for priority queue:
# https://docs.python.org/3.11/library/heapq.html#priority-queue-implementation-notes
from itertools import count
from heapq import heappush, heappop
pq = []               # list of entries arranged in a heap
entry_finder = {}     # mapping of tasks to entries
counter = count()     # unique sequence count
REMOVED = -1          # placeholder for a removed task

def reset_Q():
    global pq, entry_finder, counter
    pq = []
    entry_finder = {}
    counter = count()

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    if task in entry_finder:
        remove_task(task)
    count = next(counter)
    entry = [priority, count, task]
    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')

# drc: directions: 0=north, 1=east, 2=south, 3=west
State = namedtuple('State', ['r', 'c', 'drc', 'ndir', 'cost'])

DIRS = [0, 1, 2, 3]

def ActionsOne(A, node):
    m, n = A.shape
    r, c, drc, ndir, cost = node.r, node.c, node.drc, node.ndir, node.cost
    As = []
    for d in DIRS:
        if d == drc:
            if ndir < 3:
                if d == 0 and r > 0:    # 0 => north
                    As.append(State(r-1, c, 0, ndir+1, cost+A[r-1, c]))
                elif d == 1 and c < n-1:  # 1 => east
                    As.append(State(r, c+1, 1, ndir+1, cost+A[r, c+1]))
                elif d == 2 and r < m-1:  # 2 => south
                    As.append(State(r+1, c, 2, ndir+1, cost+A[r+1, c]))
                elif d == 3 and c > 0:    # 3 => west
                    As.append(State(r, c-1, 3, ndir+1, cost+A[r, c-1]))
            
        else: # Cannot reverse direction
            if d == 0 and drc != 2 and r > 0:    # 0 => north
                As.append(State(r-1, c, 0, 1, cost+A[r-1, c]))
            elif d == 1 and drc != 3 and c < n-1:  # 1 => east
                As.append(State(r, c+1, 1, 1, cost+A[r, c+1]))
            elif d == 2 and drc != 0 and r < m-1:  # 2 => south
                As.append(State(r+1, c, 2, 1, cost+A[r+1, c]))
            elif d == 3 and drc != 1 and c > 0:    # 3 => west
                As.append(State(r, c-1, 3, 1, cost+A[r, c-1]))
    return As

def Astar(F, A, H):
    m, n = A.shape
    # Initial state into the priority queue
    add_task(State(0, 0, -1, 0, 0))
    V = set()
    while True: # A solution does exist (!)
        s = pop_task()
        if (s.r, s.c) == (m-1, n-1):
            return s.cost
        else:
            V.add( (s.r, s.c, s.drc, s.ndir) )
            for t in F(A, s):
                if (t.r, t.c, t.drc, t.ndir) not in V: 
                    add_task( t, t.cost + H[t.r, t.c] )

# Part Two
def ActionsTwo(A, node):
    m, n = A.shape
    r, c, drc, ndir, cost = node.r, node.c, node.drc, node.ndir, node.cost
    As = []
    for d in DIRS:
        if d == drc:
            if ndir < 10:
                if d == 0 and r > 0:    # 0 => north
                    As.append(State(r-1, c, 0, ndir+1, cost+A[r-1, c]))
                elif d == 1 and c < n-1:  # 1 => east
                    As.append(State(r, c+1, 1, ndir+1, cost+A[r, c+1]))
                elif d == 2 and r < m-1:  # 2 => south
                    As.append(State(r+1, c, 2, ndir+1, cost+A[r+1, c]))
                elif d == 3 and c > 0:    # 3 => west
                    As.append(State(r, c-1, 3, ndir+1, cost+A[r, c-1]))
            
        else: # Cannot reverse direction
            if d == 0 and drc != 2 and r > 3:     # 0 => north
                As.append(State(r-4, c, 0, 4, cost+A[r-1, c]+A[r-2, c]+A[r-3, c]+A[r-4, c]))

            elif d == 1 and drc != 3 and c < n-4:  # 1 => east
                As.append(State(r, c+4, 1, 4, cost+A[r, c+1]+A[r, c+2]+A[r, c+3]+A[r, c+4]))

            elif d == 2 and drc != 0 and r < m-4:  # 2 => south
                As.append(State(r+4, c, 2, 4, cost+A[r+1, c]+A[r+2, c]+A[r+3, c]+A[r+4, c]))

            elif d == 3 and drc != 1 and c > 3:    # 3 => west
                As.append(State(r, c-4, 3, 4, cost+A[r, c-1]+A[r, c-2]+A[r, c-3]+A[r, c-4]))
    return As


def ComputeH(A):
    m, n = A.shape
    # Compute lower bounds to destination (ignore constraints)
    G = nx.DiGraph()

    for r in range(m):
        for c in range(n-1):
            G.add_edge((r, c+1), (r, c), length=A[r, c+1])  # <-

    for r in range(m):
        for c in range(1, n):
            G.add_edge((r, c), (r, c+1), length=A[r, c])  # ->

    for c in range(n):
        for r in range(m-1):
            G.add_edge((r+1, c), (r, c), length=A[r+1, c])  # |

    for c in range(n):
        for r in range(1, m):
            G.add_edge((r, c), (r+1, c), length=A[r, c])  # |

    Ds = nx.single_source_dijkstra_path_length( G, (m-1,n-1), weight="length" )

    H = zeros((m, n))
    for r in range(m):
        for c in range(n):
            H[r, c] = Ds[r,c]

    return H


def PartOne(A):
    reset_Q()
    return Astar(ActionsOne, A, ComputeH(A))

def PartTwo(A):
    reset_Q()
    return Astar(ActionsTwo, A, ComputeH(A))


def Parser(filename, F):
    fh = open(filename, mode='r', encoding='utf-8')
    return F(matrix([[int(c) for c in row.replace('\n','')] for row in fh]))


# TEST FROM COMMAND LINE
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', default='./small.txt', type=str, required=False)
args = parser.parse_args()

t0 = perf_counter() 
print('Part 1:', Parser(args.filename, PartOne), 'time:', round(perf_counter() - t0, 3))

t0 = perf_counter() 
print('Part 2:', Parser(args.filename, PartTwo), 'time:', round(perf_counter() - t0, 3))