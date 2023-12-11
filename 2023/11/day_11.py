#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

GALAXY = "#"

from itertools import combinations
from copy import copy

def manhattan(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])

def manhattan_expand(a, b, galaxies, age=1):
    x_min, x_max = min(a[0], b[0]), max(a[0], b[0])
    y_min, y_max = min(a[1], b[1]), max(a[1], b[1])
    x_values, y_values = map(set, zip(*galaxies))
    distance = 0
    for x in range(x_min+1, x_max+1):
        if x in x_values:
            distance += 1
        else:
            distance += age
    for y in range(y_min+1, y_max+1):
        if y in y_values:
            distance += 1
        else:
            distance += age
    return distance

def parse_galaxies(image_list):
    galaxies = []
    for y, l in enumerate(image_list):
        for x, g in enumerate(l.strip()):
            if g == GALAXY:
                galaxies.append((x,y))
    return galaxies

def print_galaxies(galaxies):
    x_values, y_values = map(set, zip(*galaxies))
    x_min, x_max, y_min, y_max = min(x_values), max(x_values), \
                                 min(y_values), max(y_values)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            print("#" if (x,y) in galaxies else ".", end="")
        print("")

def expand(galaxies):
    galaxies = copy(galaxies) # make a copy
    x_values, y_values = map(set, zip(*galaxies))
    x_min, x_max, y_min, y_max = min(x_values), max(x_values), \
                                 min(y_values), max(y_values)
    for y in range(y_max, y_min-1, -1): # expand backwards
        if y in y_values:
            # row not empty
            continue
        for i in range(len(galaxies)):
            if galaxies[i][1] > y:
                galaxies[i] = (galaxies[i][0], galaxies[i][1] + 1)
    for x in range(x_max, x_min-1, -1):
        if x in x_values:
            # col not empty
            continue
        for i in range(len(galaxies)):
            if galaxies[i][0] > x:
                galaxies[i] = (galaxies[i][0] + 1, galaxies[i][1])
    return galaxies

def part1(galaxies):
    sum = 0
    for c in combinations(expand(galaxies), 2):
        sum += manhattan(*c)
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
