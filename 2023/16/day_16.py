#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

DIRECTIONS = { "NW": (-1, -1), "N" : ( 0, -1), "NE": ( 1, -1),
               "W" : (-1,  0),                 "E" : ( 1,  0),              
               "SW": (-1,  1), "S" : ( 0,  1), "SE": ( 1,  1)  }    

def parse_contraption(input_lines):
    contraption = {}
    for y, l in enumerate(input_lines):
        for x, d in enumerate(l.strip()):
            if d != ".":
                contraption[(x,y)] = d
    return contraption

def grid_size(grid):
    x, y = map(set, zip(*grid.keys()))
    return min(x), max(x), min(y), max(y)

def energize(contraption, initial_beam):
    beams = [initial_beam]
    visited = set()
    x_min, x_max, y_min, y_max = grid_size(contraption)
    while len(beams):
        b = beams.pop()
        if b in visited:
            # we already went through this tile in this direction
            # -> do nothing
            continue
        if b != initial_beam: # avoid registering 1st step
            visited.add(b)
        b_pos, b_dir = b
        # move 1 step in the direction
        new_pos = b_pos[0]+DIRECTIONS[b_dir][0], b_pos[1]+DIRECTIONS[b_dir][1]
        if new_pos[0] < x_min or new_pos[0] > x_max \
           or new_pos[1] < y_min or new_pos[1] > y_max:
            # beam has exited the contraption
            continue
        if new_pos not in contraption:
            # empty cell "."
            beams.append((new_pos, b_dir))
            continue
        if contraption[new_pos] == "/":
            reflect = {"N": "E", "S": "W", "W": "S", "E": "N"}
            beams.append((new_pos, reflect[b_dir]))
        elif contraption[new_pos] == "\\":
            reflect = {"N": "W", "S": "E", "W": "N", "E": "S"}
            beams.append((new_pos, reflect[b_dir]))
        elif contraption[new_pos] == "-":
            if b_dir in ("N", "S"):
                # split horizontally
                beams.append((new_pos, "E"))
                beams.append((new_pos, "W"))
            else:
                beams.append((new_pos, b_dir))
        elif contraption[new_pos] == "|":
            if b_dir in ("E", "W"):
                # split vertically
                beams.append((new_pos, "N"))
                beams.append((new_pos, "S"))
            else:
                beams.append((new_pos, b_dir))
        else:
            raise ValueError(f'Unknown contraption device: {contraption[new_pos]}')
    energized = set(e[0] for e in visited)
    # for y in range(y_max+1):
    #     print("".join("#" if (x,y) in energized else "." for x in range(x_max+1)))
    return len(energized)

@timing
def part1(contraption):
    return energize(contraption, ((-1,0), "E"))

@timing
def part2(contraption):
    x_min, x_max, y_min, y_max = grid_size(contraption)
    energized = []
    for x in range(x_min, x_max+1):
        energized.append(energize(contraption, ((x, -1), "S")))
        energized.append(energize(contraption, ((x, y_max+1), "N")))
    for y in range(y_min, y_max+1):
        energized.append(energize(contraption, ((-1, y), "E")))
        energized.append(energize(contraption, ((x_max+1, y), "W")))
    return max(energized)


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        contraption = parse_contraption(f.readlines())
    print("Part #1 :", part1(contraption))
    print("Part #2 :", part2(contraption))
