#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from functools import cmp_to_key
from copy import deepcopy
import math

input_file = "input"
#input_file = "test01.txt"

def compare(l, r):
    """ Return -1 if l < r, 1 if l > r, 0 if equal """
    while True:
        if len(l) == 0 and len(r) == 0:
            # both lists are empty > equal
            break
        elif len(l) == 0:
            return -1
        elif len(r) == 0:
            return 1
        l1 = l.pop(0)
        r1 = r.pop(0)
        if isinstance(l1, int) and isinstance(r1, int):
            # both integers
            if l1 < r1:
                return -1
            elif l1 > r1:
                return 1
            else:
                continue
        elif isinstance(l1, list) and isinstance(r1, list):
            # both lists
            c = compare(l1, r1)
            if c == 0:
                continue
            return c
        else:
            # 1 list + 1 integer
            if isinstance(l1, int):
                l1 = [l1]
            else:
                r1 = [r1]
            c = compare(l1, r1)
            if c == 0:
                continue
            return c
    # no decision can be made - assume equality
    return 0

def compare2(l, r):
    # use deepcopies to not alter l & r
    return compare(deepcopy(l), deepcopy(r))

if __name__ == '__main__':
    with open(input_file, 'r') as f:
        x = f.read().strip()
        pairs = x.split('\n\n')
        packets = [eval(p) for p in re.split('\n\n|\n', x)]
    
    part1 = 0
    for i, p in enumerate(pairs):
        l, r = map(eval, p.strip().split('\n'))
        if compare(l, r) == -1:
            # l < r ---> correct order
            part1 += i+1

    dividers = [[[6]], [[2]]]
    for d in dividers:
        packets.insert(0, d)
    packets.sort(key=cmp_to_key(compare2))

    print("Part #1 :", part1)
    print("Part #2 :", math.prod((packets.index(d)+1 for d in dividers)))
