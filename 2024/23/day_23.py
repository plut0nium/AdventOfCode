#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from utils import timing

from collections import Counter, defaultdict


@timing
def part1(connections):
    computers = defaultdict(set)
    threes = set()
    for x in connections:
        a, b = x
        computers[a].add(b)
        computers[b].add(a)
    for c1 in computers:
        for c2 in computers[c1]:
            for c3 in computers[c2]:
                if c1 in computers[c3]:
                    threes.add(tuple(sorted((c1, c2, c3))))
    return len([t for t in threes if any(c.startswith('t') for c in t)])


@timing
def part2(connections):
    computers = defaultdict(set)
    for x in connections:
        a, b = x
        computers[a].add(b)
        computers[b].add(a)
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        connections = [tuple(s.strip().split("-")) for s in f.readlines()]
    print(part1(connections))
    print(part2(connections))
