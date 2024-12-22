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
def part2(codes):
    
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        secrets = [int(s.strip()) for s in f.readlines()]
    print(part1(secrets))
    print(part2(secrets))
