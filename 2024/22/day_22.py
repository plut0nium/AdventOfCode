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

from functools import cache
from itertools import chain
from collections import defaultdict

PRUNE = 16777216

def mix(value, secret):
    return value ^ secret

def prune(secret):
    return secret % PRUNE

def evolve(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


@timing
def part1(secrets):
    total = 0
    for s in secrets:
        for _ in range(2000):
            s = evolve(s)
        total += s
    return total


@timing
def part2(secrets):
    sequences = []
    max_bananas = 0
    for s in secrets:
        p = [s % 10, ]
        sequences.append(defaultdict(int)) 
        for i in range(2000):
            s = evolve(s)
            p.append(s % 10)
            if i >= 4:
                q = tuple(p[i-j] - p[i-j-1] for j in reversed(range(4)))
                if q in sequences[-1]:
                    # only keep the price for the first time a sequence is encountered
                    continue
                sequences[-1][q] = p[i]
                # print(p[i], q)
    for q in set(chain(*(t.keys() for t in sequences))):
        bananas = 0
        for s in sequences:
            bananas += s[q]
        max_bananas = max(max_bananas, bananas)
    return max_bananas


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        secrets = [int(s.strip()) for s in f.readlines()]
    print(part1(secrets))
    print(part2(secrets))
