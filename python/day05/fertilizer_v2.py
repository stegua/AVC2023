# -*- coding: utf-8 -*-
"""
Day 5-bis of Advent of Code, December 2023
https://adventofcode.com/

@author: gualandi
"""

# seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

from time import perf_counter

def Merge(Ps, Rs=[]):
    if Ps == []:
        return Rs
    if len(Ps) == 1:
        Rs.append(Ps[0])
        return Rs
    a,b = Ps[0]
    c,d = Ps[1]
    if b == c:
        return Merge([(a, d)] + Ps[2:], Rs)
    Rs.append( (a,b) )
    return Merge(Ps[1:], Rs)


def MergeTwo(Ps, Rs=[]):
    if Ps == []:
        return Rs
    if len(Ps) == 1:
        Rs.append(Ps[0])
        return Rs
    a, b, c = Ps[0]
    d, e, f = Ps[1]
    if c == f and b == d:
        return MergeTwo([(a, e, c)] + Ps[2:], Rs)
    Rs.append( Ps[0] )
    return MergeTwo(Ps[1:], Rs)


def Compress(Ps, Rs=[]):
    if Ps == []:
        return Rs
    if len(Ps) == 1:
        Rs.append(Ps[0])
        return Rs
    a, b = Ps[0]
    c, d = Ps[1]
    if b < c:
        Rs.append( (a,b) )
        return Compress(Ps[1:], Rs)
    e = max(b, d)
    return Compress( [(a, e)] + Ps[2:], Rs)
    

def ProcessHeader(header):
    Seed = [int(c) for c in header.split(':')[1].strip().split(' ')]
    Ps = [(Seed[i], Seed[i] + Seed[i+1]) for i in range(0, len(Seed), 2)]
    Ps.sort(key=lambda x: x[0])
    return Merge(Ps, [])
    

def ProcessBlock(block, Ps):
    Hs = block.split('\n')
    Ts = []
    for buf in Hs[1:-1]:
        if buf != '':
            dest, source, ra = list(map(int, buf.split(' ')))
            Ts.append( (source, source+ra, dest-source) )
    Ts.sort(key=lambda x: x[0])
    Ts = MergeTwo(Ts, [])
    Bs = ForwardScan(Ps, Ts, [])
    Bs.sort(key=lambda z: z[0])
    return [a for a in Compress(Bs, [])]


def ForwardScan(As, Bs, Rs):
    if As == []: return Rs
    if Bs == []: return Rs + As
    # Take two heads
    a, b = As[0]
    p, q, delta = Bs[0]

    if q <= a:
        return ForwardScan(As, Bs[1:], Rs)

    if b <= p:
        Rs.append( (a, b) )
        return ForwardScan( As[1:], Bs, Rs)

    # 1. (a, b) contained in (p, q) 
    if p <= a < b <= q:
        Rs.append( ((a+delta, b+delta)) ) 
        return ForwardScan(As[1:], Bs, Rs)
    
    # 2. (p, q) contained in (a, b)
    elif a <= p < q <= b: 
        if a < p:
            Rs.append( (a, p) )
        Rs.append( (p+delta, q+delta) )
        if q < b:
            return ForwardScan( [(q,b)]+As, Bs[1:], Rs)
        return ForwardScan( As[1:], Bs[1:], Rs)

    # 3. (a, b) before (p, q)
    elif a < p < b < q: 
        Rs.append( (a, p) )
        Rs.append( (p+delta, b+delta) )
        return ForwardScan(As[1:], Bs, Rs)

    # 4. (p, q) before (a, b)
    elif p < a < q < b: 
        Rs.append( (a+delta, q+delta))
        return ForwardScan( [(q, b)]+As[1:], Bs[1:], Rs)

    raise RuntimeError('This should not happen!')


def Parser(filename):
    t1_start = perf_counter() 
    fh = open(filename, mode='r', encoding='utf-8')
    
    Ps = ProcessHeader(fh.readline())

    fh.readline()
    block = ''
    for row in fh:
        if row == '\n':
            Ps = ProcessBlock(block, Ps)
            block = ''
        else:
            block = block + row
    if block != '':
        Ps = ProcessBlock(block, Ps)

    t1_stop = perf_counter()
    print("AoC 2023 - Day 5 part 2, solved in", round(t1_stop - t1_start, 3), "seconds!")
    return Ps[0][0]

# Check for PartOne (Lost!)
#print('Solution 1:', Parser('input.txt'))

# Check for PartTwo
print('Solution 2:', Parser('input.txt'))
