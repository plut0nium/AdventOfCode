#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from copy import deepcopy

input_file = "input"
#input_file = "test01.txt"

pattern_move = re.compile(r"move (\d+) from (\d+) to (\d+)")
pattern_crate = re.compile(r"\[([A-Z])\] ?|[ ]{3,4}")

if __name__ == '__main__':
    with open(input_file) as f:
        a, b = f.read().rstrip().split("\n\n")
    c = a.split("\n")
    n = len(c.pop().strip().split())
    stacks = [[] for _ in range(n)]
    for d in reversed(c): # crates stacks
        y = pattern_crate.findall(d)
        for i in range(len(y)):
            if len(y[i]):
                stacks[i].append(y[i])
    stacks2 = deepcopy(stacks)
    for m in b.split("\n"): # moves
        z = pattern_move.match(m)
        n = int(z.group(1))     # number of crates
        f = int(z.group(2)) - 1 # from
        t = int(z.group(3)) - 1 # to
        # part 1
        for i in range(n):
            stacks[t].append(stacks[f].pop())
        # part 2
        stacks2[t] += stacks2[f][-n:]
        stacks2[f] = stacks2[f][:-n]

    print("Part #1 :", "".join((s[-1] for s in stacks)))
    print("Part #2 :", "".join((s[-1] for s in stacks2)))
