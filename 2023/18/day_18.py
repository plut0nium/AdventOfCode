#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

DIRS = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}

def parse_plan(input_lines):
    plan = []
    for l in input_lines:
        direction, count, color = l.strip().split()
        plan.append((direction, int(count), color[1:-1]))
    return plan

def grid_size(g):
    x, y = map(set, zip(*g.keys()))
    return min(x), max(x), min(y), max(y)

@timing
def part1(plan, start_pos=(0,0)):
    current_pos = start_pos
    trench = {current_pos: "#"}
    lagoon_size = 0
    for p in plan:
        for _ in range(p[1]):
            current_pos = (current_pos[0]+DIRS[p[0]][0], current_pos[1]+DIRS[p[0]][1])
            trench[current_pos] = "#"
    x_min, x_max, y_min, y_max = grid_size(trench)
    for y in range(y_min, y_max+1):
        pass
    return lagoon_size

@timing
def part2(plan):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        plan = parse_plan(f.readlines())
    print("Part #1 :", part1(plan))
    print("Part #2 :", part2(plan))
