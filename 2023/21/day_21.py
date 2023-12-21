#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

DIRS = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}
START = "S"
ROCK = "#"

def parse_garden(input_lines):
    garden = {}
    start_pos = None
    for y, l in enumerate(input_lines):
        for x, p in enumerate(l.strip()):
            if p == ROCK:
                garden[x,y] = p
            elif p == START:
                start_pos = (x,y)
    return garden, start_pos

def grid_size(g):
    x, y = map(set, zip(*g.keys()))
    return min(x), max(x), min(y), max(y)

def garden_size(g):
    # garden has a blank padding around it
    x_min, x_max, y_min, y_max = grid_size(g)
    return x_min-1, x_max+1, y_min-1, y_max+1 

@timing
def part1(garden, start_pos, steps=6):
    pos = [{start_pos}]
    x_min, x_max, y_min, y_max = garden_size(garden)
    for s in range(steps):
        pos.append(set())
        for p in pos[-2]:
            for d in DIRS.values():
                pos_next = (p[0]+d[0], p[1]+d[1])
                if x_min <= pos_next[0] <= x_max \
                   and y_min <= pos_next[1] <= y_max \
                   and pos_next not in garden:
                    pos[-1].add(pos_next)
    return len(pos[-1])

@timing
def part2(garden, start_pos, steps=10):
    pos = [{start_pos}]
    x_min, x_max, y_min, y_max = garden_size(garden)
    for s in range(steps):
        pos.append(set())
        for p in pos[-2]:
            for d in DIRS.values():
                pos_next = (p[0]+d[0], p[1]+d[1])
                if pos_next not in garden:
                    pos[-1].add(pos_next)
    return len(pos[-1])


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        garden, start_pos = parse_garden(f.readlines())
    print("Part #1 :", part1(garden, start_pos, 64))
    print("Part #2 :", part2(garden, start_pos))
