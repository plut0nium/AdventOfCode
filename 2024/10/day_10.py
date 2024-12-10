#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)] # N > E > S > W


def find_trailheads(topographic_map):
    trailheads = set()
    for y, r in enumerate(topographic_map):
        for x, h in enumerate(r):
            if h == 0:
                trailheads.add((x,y))
    return trailheads


def ascend(topographic_map, start):
    x, y = start
    reached = set() # part 1
    rating = 0      # part 2
    
    if topographic_map[y][x] == 9:
        return set([(x,y)]), 1
    
    for d in DIRS:
        x_next = x + d[0]
        y_next = y + d[1]
        if not (0 <= x_next < len(topographic_map[0])) \
           or not (0 <= y_next < len(topographic_map)):
            # out of map
            continue
        if (topographic_map[y_next][x_next] - topographic_map[y][x]) == 1:
            a, b = ascend(topographic_map, (x_next, y_next))
            reached.update(a)
            rating += b
    return reached, rating


def part1_2(topographic_map):
    trailheads = find_trailheads(topographic_map)
    total_score = 0
    total_rating = 0
    for t in trailheads:
        total_score += len(ascend(topographic_map, t)[0])
        total_rating += ascend(topographic_map, t)[1]
    return total_score, total_rating


def part2(topographic_map):
    return None


if __name__ == '__main__':
    topographic_map = []
    with open(input_file, 'r') as f:
        for l in f.readlines():
            topographic_map.append([])
            for p in l.strip():
                topographic_map[-1].append(int(p))
    for r in part1_2(topographic_map):
        print(r)
