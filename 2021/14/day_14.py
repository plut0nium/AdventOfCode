#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter
import time

input_file = "input"
#input_file = "test1.txt"

template = None
reactions = {}

def polymerize(p, reactions):
    # naive solution for part1
    p2 = ""
    for i in range(len(p)-1):
        if p[i:i+2] in reactions:
            p2 += p[i] + reactions[p[i:i+2]]
        else: # not used if i'm correct
            p2 += p[i]
    # add the last char
    p2 += p[-1]
    return p2

def poly2(p, reactions):
    # 'optimized' pair counting for part 2
    p2 = Counter()
    for x in p.keys():
        a = x[0] + reactions[x]
        b = reactions[x] + x[1]
        p2[a] += p[x]
        p2[b] += p[x]
    return p2

def part1(template, reactions, steps):
    p = template
    for i in range(steps):
        p = polymerize(p, reactions)
    
    elements = set(p)
    c = [p.count(e) for e in elements]
    return max(c) - min(c)

def part2(template, reactions, steps):
    p = Counter()
    for i in range(len(template)-1):
        p[template[i:i+2]] += 1
    for i in range(steps):
        p = poly2(p, reactions)

    c = []
    elements = set(e for r in p for e in r)
    for e in elements:
        d = 0
        for pair in p.keys():
            if e*2 == pair:
                d += p[pair] * 2
            elif e in pair:
                d += p[pair]
        if e in (template[0], template[-1]):
            # every 'atom' is counted twice, except first and last
            d += 1
        c.append(int(d/2))
    return max(c) - min(c)


if __name__ == '__main__':
    timing = {}
    timing['start'] = time.time()
    with open(input_file,'r') as f:
        template = f.readline().strip()
        _ = f.readline()
        for l in f.readlines():
            a,b = l.strip().split(" -> ")
            reactions[a] = b
    
    timing['part1'] = time.time()
    print(part1(template, reactions, 10))
    timing['part2'] = time.time()
    print(part2(template, reactions, 40))
    timing['end'] = time.time()
    # print(f"Parsing: {(timing['part1'] - timing['start']) * 1000:.3f} ms")
    # print(f"Part 1:  {(timing['part2'] - timing['part1']) * 1000:.3f} ms")
    # print(f"Part 2:  {(timing['end'] - timing['part2']) * 1000:.3f} ms")
