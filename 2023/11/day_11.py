#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

GALAXY = "#"

from itertools import combinations

def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def manhattan_expand(a, b, galaxies, age=1):
    x_min, x_max = min(a[0], b[0]), max(a[0], b[0])
    y_min, y_max = min(a[1], b[1]), max(a[1], b[1])
    x_values, y_values = map(set, zip(*galaxies))
    distance = manhattan(a, b)
    for x in set(range(x_min, x_max+1)) - x_values:
        distance += age - 1
    for y in set(range(y_min, y_max+1)) - y_values:
        distance += age - 1
    return distance

def parse_galaxies(image_list):
    galaxies = []
    for y, l in enumerate(image_list):
        for x, g in enumerate(l.strip()):
            if g == GALAXY:
                galaxies.append((x,y))
    return galaxies

def part1(galaxies):
    sum = 0
    for c in combinations(galaxies, 2):
        sum += manhattan_expand(c[0], c[1], galaxies, 2)
    return sum

def part2(galaxies):
    sum = 0
    for c in combinations(galaxies, 2):
        sum += manhattan_expand(c[0], c[1], galaxies, 1_000_000)
    return sum


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        galaxies = parse_galaxies(f.readlines())
    print("Part #1 :", part1(galaxies))
    print("Part #2 :", part2(galaxies))
