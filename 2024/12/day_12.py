#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


from collections import defaultdict, Counter

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)] # N > E > S > W


def part1(garden):
    plants = defaultdict(set)
    for y, row in enumerate(garden):
        for x, p in enumerate(row):
            plants[p].add((x, y))
    regions = []    
    for plant, plots in plants.items():
        while len(plots):
            p = plots.pop()
            to_explore = set([p])
            region = set()
            perim = 0
            while to_explore:
                p = to_explore.pop()
                region.add(p)
                adjacent = []
                for d in DIRS:
                    x_next = p[0] + d[0]
                    y_next = p[1] + d[1]
                    if not (0 <= x_next < len(garden[0])) \
                       or not (0 <= y_next < len(garden)):
                        # out of map
                        continue
                    if (x_next, y_next) in plots:
                        # not yet explored + same plant -> to explore
                        to_explore.add((x_next, y_next))
                        plots.remove((x_next, y_next))
                    elif (x_next, y_next) in region:
                        # same plant + already explored -> adjacent
                        adjacent.append((x_next, y_next))
                perim += 4 - (2 * len(adjacent))
            regions.append((plant, region, perim))
    return sum(len(r[1]) * r[2] for r in regions)


def part2(stones):

    return None


if __name__ == '__main__':
    garden = []
    with open(input_file, 'r') as f:
        for r in f.readlines():
            garden.append(r.strip())
    test = part1(garden)
    print(part1(garden))
    print(part2(garden))
