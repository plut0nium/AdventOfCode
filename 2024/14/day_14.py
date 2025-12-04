#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


from itertools import batched
from collections import Counter
from functools import reduce
import re
import png
from statistics import variance

if "test" in input_file:
    SPACE_SIZE = (11, 7)
else:
    SPACE_SIZE = (101, 103)


def print_robots(robots, space_size):
    robots_counter = Counter(p for p in robots.values())
    for y in range(space_size[1]):
        for x in range(space_size[0]):
            if (x,y) in robots_counter:
                print(robots_counter[(x,y)], end="")
            else:
                print(".", end="")
        print()


def render_robots(robots, space_size, filename):
    BLACK_PIXEL = (0, 0, 0)
    WHITE_PIXEL = (255, 255, 255)
    width, height = space_size
    robots = set(robots)
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            if (x,y) in robots:
                row = row + WHITE_PIXEL
            else:
                row = row + BLACK_PIXEL
            # row = row + (x, max(0, 255 - x - y), y)
        img.append(row)
    with open(filename + '.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)


def safety_factor(robots, space_size):
    robots_per_quadrant = []
    quadrants = [((0, space_size[0]//2), (0, space_size[1]//2)),
                 ((space_size[0]//2 + 1, space_size[0]), (0, space_size[1]//2)),
                 ((0, space_size[0]//2), (space_size[1]//2 + 1, space_size[1])),
                 ((space_size[0]//2 + 1, space_size[0]), (space_size[1]//2 + 1, space_size[1]))]
    for x_range,y_range in quadrants:
        robots_per_quadrant.append(len([p for p in robots.values() if p[0] in range(*x_range) and p[1] in range(*y_range)]))
    return reduce(lambda a,b: a*b, robots_per_quadrant)


def move_robots(robots, space_size):
    for r, p in robots.items():
        _, vel = r
        x_next, y_next = p[0] + vel[0], p[1] + vel[1]
        if x_next < 0:
            x_next += space_size[0]
        elif x_next >= space_size[0]:
            x_next -= space_size[0]
        if y_next < 0:
            y_next += space_size[1]
        elif y_next >= space_size[1]:
            y_next -= space_size[1]
        robots[r] = (x_next, y_next)


@timing
def part1(robots, space_size):
    for _ in range(100):
        move_robots(robots, space_size)
    #print_robots(robots, space_size)
    return safety_factor(robots, space_size)


@timing
def part2(robots, space_size):
    var = []
    for _ in range(10_000):
        move_robots(robots, space_size)
        xvar = variance(p[0] for p in robots.values())
        yvar = variance(p[1] for p in robots.values())
        var.append((xvar, yvar))
    s = [sum(v) for v in var]
    found_tree_index = s.index(min(s)) + 101 # account for 100 steps in part 1 (+ initial state)
    render_robots(list(robots.values()), space_size, 'tree')
    return found_tree_index


if __name__ == '__main__':
    robots = {}
    with open(input_file, 'r') as f:
        for r in f.readlines():
            initial = tuple(batched(map(int, re.findall(r'(-?\d+)', r)), 2))
            robots[initial] = initial[0]
    print(part1(robots, SPACE_SIZE))
    print(part2(robots, SPACE_SIZE))
