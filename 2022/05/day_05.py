#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from copy import deepcopy

input_file = "input"
#input_file = "test01.txt"

pattern_move = re.compile(r"move (\d+) from (\d+) to (\d+)")
pattern_crate = re.compile(r"\[([A-Z])\]|[ ]{3,4}")

if __name__ == '__main__':
    with open(input_file) as f:
        a, b = f.read().rstrip().split("\n\n")
    c = a.split("\n")
    n = len(c.pop().strip().split())
    stacks = [[] for _ in range(n)]
    for d in reversed(c):
        y = pattern_crate.findall(d)
        for i in range(len(y)):
            if len(y[i]):
                stacks[i].append(y[i])
    stacks2 = deepcopy(stacks)
    for l in b.split("\n"):
        z = pattern_move.match(l)
        m = tuple(map(int, z.groups()))
        # part 1
        for i in range(m[0]):
            stacks[m[2]-1].append(stacks[m[1]-1].pop())
        # part 2
        stacks2[m[2]-1] += stacks2[m[1]-1][-m[0]:]
        stacks2[m[1]-1] = stacks2[m[1]-1][:-m[0]]

    print("Part #1 :", "".join((s[-1] for s in stacks)))
    print("Part #2 :", "".join((s[-1] for s in stacks2)))
