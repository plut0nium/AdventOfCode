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

from collections import Counter

def mix(value, secret):
    return value ^ secret

def prune(secret):
    return secret % 16777216

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
    sequences_all = Counter()
    for s in secrets:
        prev = s % 10 # initial price
        price_change = []
        sequences = Counter()
        for i in range(2000):
            s = evolve(s)
            price = s % 10
            price_change.append(price - prev)
            prev = price
            if len(price_change) >= 4:
                q = tuple(price_change[-4:]) # get the last 4
                if q in sequences:
                    # only keep the price for the first time a sequence is encountered
                    continue
                sequences[q] = price
        sequences_all.update(sequences)
    return max(sequences_all.values())


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        secrets = [int(s.strip()) for s in f.readlines()]
    print(part1(secrets))
    print(part2(secrets))
