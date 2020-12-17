#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product
from collections import Counter
from datetime import datetime
from operator import add

def conway_cubes(initial_space, dimensions=3, loop=6):
    space = set()
    for c in initial_space:
        space.add(c + (0,)*(dimensions-len(c)))
    directions = [d for d in product([-1,0,1], repeat=dimensions) if d != (0,)*dimensions]
    for i in range(loop):
        space_new = set()
        neighbour_count = Counter()
        for x in space:
            for d in directions:
                neighbour_count[tuple(map(add, x, d))] += 1
        for c in neighbour_count.items():
            if c[1] == 3 or (c[0] in space and c[1] == 2):
                space_new.add(c[0])
        space = space_new
    return len(space)


input_file = "input"
#input_file = "test1.txt"

if __name__ == '__main__':
    space = set()
    x,y = 0,0

    with open(input_file,'r') as f:
        for r in [l.strip() for l in f.readlines() if l.strip()]:
            for c in r:
                if c == '#':
                    space.add((x,y))
                x += 1
            y+= 1
            x = 0

    # print("Step 1:", conway_cubes(space, 3))
    # print("Step 2:", conway_cubes(space, 4))

    # let's do some measurements...
    for n in range(2,6):
        start_time = datetime.now()
        print("n = {}:".format(n), conway_cubes(space, n), " -> ", datetime.now() - start_time)
