#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from collections import Counter

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

dirs = { 'N': ( 0,-1), 'NW': (-1,-1), 'NE': ( 1,-1),
         'S': ( 0, 1), 'SW': (-1, 1), 'SE': ( 1, 1),
         'W': (-1, 0), 
         'E': ( 1, 0) }

moves = [('N', 'NW', 'NE'), ('S', 'SW', 'SE'),
         ('W', 'NW', 'SW'), ('E', 'NE', 'SE')]

grid = {}

def size(grid):
    xmin, xmax = min(c[0] for c in grid.keys()), max(c[0] for c in grid.keys())
    ymin, ymax = min(c[1] for c in grid.keys()), max(c[1] for c in grid.keys())
    return xmin, xmax, ymin, ymax

def display(grid):
    xmin, xmax, ymin, ymax = size(grid)
    for y in range(ymin, ymax+1):
        l = ''
        for x in range(xmin, xmax+1):
            l += grid[(x,y)] if (x,y) in grid else '.'
        print(l)

def count_ground(grid):
    xmin, xmax, ymin, ymax = size(grid)
    return (abs(xmax - xmin) +1 ) * (abs(ymax - ymin) + 1) - len(grid)


if __name__ == '__main__':
    start_time = time()
    with open(input_file, 'r') as f:
        for y, l in enumerate(f.readlines()):
            for x, c in enumerate(l):
                if c == '#':
                    grid[(x,y)] = c
    m = 0
    p1 = 0
    while True:
    # for _ in range(10):
        for p, e in grid.items():
            c = None
            if any((p[0]+d[0],p[1]+d[1]) in grid for d in dirs.values()):
                # neighbour found -> move
                for i in range(4):
                    j = (i + m) % 4
                    if all((p[0]+dirs[d][0],p[1]+dirs[d][1]) not in grid for d in moves[j]):
                        # all cells are free -> can move in this direction
                        c = (p[0]+dirs[moves[j][0]][0],p[1]+dirs[moves[j][0]][1])
                        break
            grid[p] = c if c is not None else '#'
        candidates = Counter(grid.values())
        if len(candidates) == 1:
            # PART2 : no elve will move -> finished
            break
        for p, e in list(grid.items()):
            if e == '#':
                continue
            elif candidates[e] == 1:
                # move
                grid[e] = '#'
                del grid[p]
            else:
                # dont move
                grid[p] = '#'
        m += 1
        if m == 10:
            p1 = count_ground(grid)

    print("Part #1 :", p1)
   
    print("Part #2 :", m+1)
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
