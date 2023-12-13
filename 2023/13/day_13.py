#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

ASH = "."
ROCK = "#"

from collections import defaultdict

def parse_patterns(input_lines):
    patterns = [{}]
    y_offset = 0
    for y, l in enumerate(input_lines):
        l = l.strip()
        if len(l):
            for x, c in enumerate(l):
                if c == ROCK:
                    patterns[-1][(x,y - y_offset)] = c
        else:
            patterns.append({})
            y_offset = y + 1
    return patterns

def grid_size(g):
    x, y = map(set, zip(*g.keys()))
    return min(x), max(x), min(y), max(y)

def print_pattern(p):
    x_min, x_max, y_min, y_max = grid_size(p)
    for y in range(y_min, y_max+1):
        print("".join(p[(x,y)] if (x,y) in p else ASH for x in range(x_min, x_max+1)))

def get_x_values(p, y):
    return set(t[0] for t in p.keys() if t[1]==y)

def get_y_values(p, x):
    return set(t[1] for t in p.keys() if t[0]==x)

def fold(p, v, y_axis=False):
    # folds pattern p along v|v+1 on x_axis, unless y_axis is True
    x_min, x_max, y_min, y_max = grid_size(p)
    if not y_axis:
        if v not in range(x_min, x_max):
            raise ValueError(f'Value {v} out of X-range: {x_min}-{x_max}')
        extent = min((v+1)-x_min, x_max-v)
        return all(get_y_values(p, v-e) == get_y_values(p, (v+1)+e) for e in range(extent))
    else:
        if v not in range(y_min, y_max):
            raise ValueError(f'Value {v} out of Y-range: {y_min}-{y_max}')
        extent = min((v+1)-y_min, y_max-v)
        return all(get_x_values(p, v-e) == get_x_values(p, (v+1)+e) for e in range(extent))
    return False

def part1(patterns):
    total = 0
    for i, p in enumerate(patterns):
        is_folded = False
        x_min, x_max, y_min, y_max = grid_size(p)
        for x in range(x_min, x_max):
            if fold(p, x):
                total += x + 1
                is_folded = True
                break
        if is_folded:
            continue
        for y in range(y_min, y_max):
            if fold(p, y, y_axis = True):
                total += (y + 1) * 100
                is_folded = True
                break
    return total

def part2(patterns):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        patterns = parse_patterns(f.readlines())
    print("Part #1 :", part1(patterns))
    print("Part #2 :", part2(patterns))
