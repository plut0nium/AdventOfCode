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
    garden_size = (x+1,y+1)
    return garden, start_pos, garden_size

@timing
def part1(garden, start_pos, size, steps=6):
    pos = [{start_pos}]
    for s in range(steps):
        pos.append(set())
        for p in pos[-2]:
            for d in DIRS.values():
                pos_next = (p[0]+d[0], p[1]+d[1])
                if pos_next not in garden:
                    pos[-1].add(pos_next)
    return len(pos[-1])

@timing
def part2(garden):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        garden, start_pos, size = parse_garden(f.readlines())
    print("Part #1 :", part1(garden, start_pos, size, 64))
    print("Part #2 :", part2(garden))
