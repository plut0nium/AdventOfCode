#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
input_file = "test01.txt"
# input_file = "test02.txt"

DIRS = {"U": (0,-1), "D": (0,1), "L": (-1,0), "R": (1,0)}

def parse_plan(input_lines):
    plan = []
    for l in input_lines:
        direction, count, color = l.strip().split()
        plan.append((direction, int(count), color[1:-1]))
    return plan

def hex_to_dig(color):
    dir_index = ["R", "D", "L", "U"]
    direction = dir_index[int(color[-1])]
    distance = int(color[1:-1], base=16)
    return direction, distance

def grid_size(g):
    x, y = map(set, zip(*g.keys()))
    return min(x), max(x), min(y), max(y)

@timing
def part1(plan, start_pos=(0,0)):
    current_pos = start_pos
    trench = {current_pos: "#"}
    for p in plan:
        for _ in range(p[1]):
            current_pos = (current_pos[0]+DIRS[p[0]][0], current_pos[1]+DIRS[p[0]][1])
            trench[current_pos] = "#"
    x_min, x_max, y_min, y_max = grid_size(trench)
    
    stack = [(x_min-1, y_min-1)]
    expand = set()
    while len(stack):
        c = stack.pop()
        expand.add(c)
        for d in DIRS.values():
            c_next = (c[0]+d[0], c[1]+d[1])
            if c_next in trench or c_next in expand:
                continue
            elif c_next[0] < x_min-1 or c_next[0] > x_max+1 \
                 or c_next[1] < y_min-1 or c_next[1] > y_max+1:
                continue
            stack.append(c_next)
    return (x_max - x_min + 3) * (y_max - y_min + 3) - len(expand)

@timing
def part2(plan):
    for p in plan:
        direction, distance = hex_to_dig(p[2])
        # print(direction, distance)
        pass
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        plan = parse_plan(f.readlines())
    print("Part #1 :", part1(plan))
    print("Part #2 :", part2(plan))
