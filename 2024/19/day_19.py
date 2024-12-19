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
    # todo
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        p_str, d_str = f.read().split("\n\n")
        patterns = set(p_str.strip().split(", "))
        designs = d_str.strip().splitlines()
    print(part1(designs, patterns))
    print(part2(designs, patterns))
