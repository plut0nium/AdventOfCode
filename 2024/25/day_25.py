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

import re
from collections import deque
from itertools import product


@timing
def part1(locks, keys):
    fit_count = 0
    for l,k in product(locks, keys):
        assert len(l) == len(k)
        if all(l[i] + k[i] <= 5 for i in range(len(l))):
            fit_count += 1
    return fit_count


@timing
def part2(locks, keys):

    return None


if __name__ == '__main__':
    keys = []
    locks = []
    with open(input_file, 'r') as f:
        for k in f.read().split("\n\n"):
            k = k.splitlines()
            kcount = tuple([k[j][i] for j in range(len(k))].count("#") - 1 for i in range(len(k[0])))
            if k[0].startswith("."):
                keys.append(kcount)
            elif k[0].startswith("#"):
                locks.append(kcount)
            else:
                raise ValueError("Unknown input type")
            for i in range(len(k[0])):
                pass
    print(part1(locks, keys))
    print(part2(locks, keys))
