#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import defaultdict
from itertools import combinations


def in_grid(x, y, grid_size):
    return (0 <= x < grid_size[0]) and (0 <= y < grid_size[1])


def print_antinodes(antinodes, grid_size):
    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            if (x,y) in antinodes:
                print("#", end="")
            else:
                print(".", end="")
        print()


def find_antinodes(dipole, grid_size, repeat=False):
    antinodes = set()
    a, b = dipole
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    i, j = 0, 0
    if not repeat:
        # antennas are not AN
        i, j = 1, 1
    while True:
        an1 = ((a[0] + i * dx), (a[1] + i * dy))
        if not in_grid(*an1, grid_size):
            break
        antinodes.add(an1)
        if not repeat:
            # only run once
            break
        i += 1
    while True:
        an2 = ((b[0] - j * dx), (b[1] - j * dy))
        if not in_grid(*an2, grid_size):
            break
        antinodes.add(an2)
        if not repeat:
            # only run once
            break
        j += 1
    return antinodes


def part1(antennas, grid_size):
    antinodes = set()
    for freq in antennas.keys():
        for dipole in combinations(antennas[freq], 2):
            antinodes.update(find_antinodes(dipole, grid_size))
    return len(antinodes)


def part2(antennas):
    antinodes = set()
    for freq in antennas.keys():
        for dipole in combinations(antennas[freq], 2):
            antinodes.update(find_antinodes(dipole, grid_size, repeat=True))
    return len(antinodes)


if __name__ == '__main__':
    antennas = defaultdict(list)
    with open(input_file, 'r') as f:
        for y, l in enumerate(f.readlines()):
            for x, v in enumerate(l.strip()):
                if v != ".":
                    antennas[v].append((x,y))
        grid_size = (x+1,y+1)
    print(part1(antennas, grid_size))
    print(part2(antennas))
