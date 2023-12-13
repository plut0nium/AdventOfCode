#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

ASH = "."
ROCK = "#"

from copy import copy

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
        # if v not in range(x_min, x_max):
        #     raise ValueError(f'Value {v} out of X-range: {x_min}-{x_max}')
        extent = min((v+1)-x_min, x_max-v)
        return all(get_y_values(p, v-e) == get_y_values(p, (v+1)+e) for e in range(extent))
    else:
        # if v not in range(y_min, y_max):
        #     raise ValueError(f'Value {v} out of Y-range: {y_min}-{y_max}')
        extent = min((v+1)-y_min, y_max-v)
        return all(get_x_values(p, v-e) == get_x_values(p, (v+1)+e) for e in range(extent))
    return False

def find_reflection(p):
    reflection_lines = []
    x_min, x_max, y_min, y_max = grid_size(p)
    for x in range(x_min, x_max):
        if fold(p, x):
            reflection_lines.append((x,None))
    for y in range(y_min, y_max):
        if fold(p, y, y_axis = True):
            reflection_lines.append((None,y))
    return reflection_lines

def summarize(notes):
    total = 0
    for n in  notes:
        total += n[0] + 1 if n[0] is not None else (n[1] + 1) * 100
    return total

def part1(patterns):
    reflection_lines = []
    for p in patterns:
        p_lines = find_reflection(p)
        assert(len(p_lines) == 1) # only 1 reflection line per pattern in part 1
        reflection_lines.extend(p_lines)
    return summarize(reflection_lines)

def part2(patterns):
    reflection_lines = []
    for p in patterns:
        original_lines = find_reflection(p)
        current_lines = set()
        x_min, x_max, y_min, y_max = grid_size(p)
        for y_fix in range(0, y_max+1):
            for x_fix in range(0, x_max+1):
                # since we only store ROCK coordinates
                # this assumes there are no empty (i.e. ASH only) rows/cols
                # at the extremities of the patterns -> not always true
                p_fixed = copy(p)
                # fix a smudge at x,y
                if (x_fix,y_fix) in p_fixed:
                    p_fixed.pop((x_fix,y_fix))
                else:
                    p_fixed[(x_fix,y_fix)] = ROCK
                current_lines.update(find_reflection(p_fixed))
        reflection_lines.extend(f for f in current_lines.difference(original_lines))
    return summarize(reflection_lines)


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        patterns = parse_patterns(f.readlines())
    print("Part #1 :", part1(patterns))
    print("Part #2 :", part2(patterns))
