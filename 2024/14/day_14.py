#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def print_robots(robots, space_size):
    robots_counter = Counter(p[-1] for p in robots.values())
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
    # robots_pos = set(p[-1] for p in robots.values())
    robots_pos = robots[:]
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            if (x,y) in robots_pos:
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
        robots_per_quadrant.append(len([p[-1] for p in robots.values() if p[-1][0] in range(*x_range) and p[-1][1] in range(*y_range)]))
    return reduce(lambda a,b: a*b, robots_per_quadrant)


def part1(robots, space_size):
    for i in range(100):
        for r, p in robots.items():
            ipos, vel = r
            pos = p[-1]
            x_next, y_next = pos[0] + vel[0], pos[1] + vel[1]
            if x_next < 0:
                x_next += space_size[0]
            elif x_next >= space_size[0]:
                x_next -= space_size[0]
            if y_next < 0:
                y_next += space_size[1]
            elif y_next >= space_size[1]:
                y_next -= space_size[1]
            p.append((x_next, y_next))
    #print_robots(robots, space_size)
    return safety_factor(robots, space_size)


def part2(robots, space_size):
    var = []
    for i in range(10_000):
        for r, p in robots.items():
            ipos, vel = r
            pos = p[-1]
            x_next, y_next = pos[0] + vel[0], pos[1] + vel[1]
            if x_next < 0:
                x_next += space_size[0]
            elif x_next >= space_size[0]:
                x_next -= space_size[0]
            if y_next < 0:
                y_next += space_size[1]
            elif y_next >= space_size[1]:
                y_next -= space_size[1]
            p.append((x_next, y_next))
        if i > 5000:
            xvar = variance(p[-1][0] for p in robots.values())
            yvar = variance(p[-1][1] for p in robots.values())
            var.append((xvar, yvar))
    s = [sum(v) for v in var]
    found_tree_index = s.index(min(s)) + 5001 + 100 + 1
    render_robots([r[found_tree_index] for r in robots.values()], space_size, 'tree')
    return found_tree_index


if __name__ == '__main__':
    robots = {}
    with open(input_file, 'r') as f:
        for r in f.readlines():
            initial = tuple(batched(map(int, re.findall(r'(-?\d+)', r)), 2))
            robots[initial] = [initial[0]]
        if "test" in input_file:
            space_size = (11, 7)
        else:
            space_size = (101, 103)
    print(part1(robots, space_size))
    print(part2(robots, space_size))
