#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

ROUND = "O"
SQUARE = "#"
EMPTY = "."

CYCLES_COUNT = 1_000_000_000

DIRECTIONS = { "NW": (-1, -1), "N" : ( 0, -1), "NE": ( 1, -1),
               "W" : (-1,  0),                 "E" : ( 1,  0),              
               "SW": (-1,  1), "S" : ( 0,  1), "SE": ( 1,  1)
             }

from copy import copy
from functools import cache

def parse_rocks(input_lines):
    rocks = {}
    for y, l in enumerate(input_lines):
        for x, r in enumerate(l.strip()):
            if r in (ROUND, SQUARE):
                rocks[(x,y)] = r
    return rocks

def grid_size(g):
    x, y = map(set, zip(*g.keys()))
    return min(x), max(x), min(y), max(y)

def print_rocks(p):
    x_min, x_max, y_min, y_max = grid_size(p)
    for y in range(y_min, y_max+1):
        print("".join(p[(x,y)] if (x,y) in p else EMPTY for x in range(x_min, x_max+1)))

def tilt(rocks, d="N"):
    x_min, x_max, y_min, y_max = grid_size(rocks)
    while True:
        moved = 0
        for y in range(y_min, y_max+1):
            for x in range(x_min, x_max+1):
                if (x,y) not in rocks or rocks[(x,y)] == SQUARE:
                    continue
                x_dest, y_dest = (x + DIRECTIONS[d][0], y + DIRECTIONS[d][1])
                if x_dest < x_min or x_dest > x_max \
                   or y_dest < y_min or y_dest > y_max:
                    continue
                if (x_dest, y_dest) not in rocks:
                    rocks[(x_dest, y_dest)] = ROUND
                    rocks.pop((x,y))
                    moved += 1
        if not moved:
            break
    return rocks

def calc_load(rocks, d="N"):
    x_min, x_max, y_min, y_max = grid_size(rocks)
    load = 0
    for c, r in rocks.items():
        if r != ROUND:
            continue
        load += y_max - c[1] + 1
    return load

def cycle(rocks):
    for d in ("N", "W", "S", "E"):
        rocks = tilt(rocks, d)
    return rocks

def part1(rocks):
    rocks = tilt(rocks)
    # print_rocks(rocks)
    return calc_load(rocks)

def part2(rocks, n=CYCLES_COUNT):
    moved = []
    for i in range(n):
        rocks_previous = set(c for c, r in rocks.items() if r == ROUND)
        rocks = cycle(rocks)
        m = set(c for c, r in rocks.items() if r == ROUND) - rocks_previous
        if m in moved:
            # we found a cycle
            l = len(moved[moved.index(m):]) # cycle length
            # get the offset of the configuration corresponding to CYCLES_COUNT
            r = (CYCLES_COUNT - (i+1)) % l
            break
        # cache the last results
        moved.append(m)
        if len(moved) > 100:
            moved.pop(0)
    for j in range(r):
        # cycle for r additional steps
        rocks = cycle(rocks)
        # print(i+j+1, calc_load(rocks))
    return calc_load(rocks)


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        rocks = parse_rocks(f.readlines())
    print("Part #1 :", part1(rocks))
    print("Part #2 :", part2(rocks))
