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


@timing
def part1(designs, patterns):
    max_pattern_length = max(len(p) for p in patterns)
    possible = set()
    for d in designs:
        is_possible = False
        tested = set()
        remain = [d]
        while len(remain):
            r = remain.pop()
            if r in tested:
                continue
            tested.add(r)
            for i in range(1, max_pattern_length+1):
                if r[:i] in patterns:
                    if len(r[i:]) == 0:
                        possible.add(d)
                        is_possible = True
                        break
                    remain.append(r[i:])
            if is_possible:
                break
    return len(possible)


@timing
def part2(designs, patterns):
    max_pattern_length = max(len(p) for p in patterns)

    @cache
    def count_possible(s):
        if len(s) == 1:
            if s in patterns:
                return 1
            return 0
        # len(s) > 1
        total = 0
        if s in patterns:
            total += 1
        for i in range(1, min(len(s), max_pattern_length)+1):
            if s[:i] in patterns:
                total += count_possible(s[i:])
        return total
 
    return sum(count_possible(d) for d in designs)


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        p_str, d_str = f.read().split("\n\n")
        patterns = set(p_str.strip().split(", "))
        designs = d_str.strip().splitlines()
    print(part1(designs, patterns))
    print(part2(designs, patterns))
