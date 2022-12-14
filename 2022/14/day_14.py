#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test01.txt"

SAND_SOURCE = (500,0)
MOVES = [(0,1), (-1,1), (1,1)]

if __name__ == '__main__':
    cave = defaultdict(lambda: None)
    for l in open(input_file, 'r').readlines():
        r = [tuple(map(int, c.split(','))) for c in l.strip().split(' -> ')]
        for i in range(1,len(r)):
            r1 = r[i-1]
            r2 = r[i]
            if r1[0] == r2[0]:
                # same X
                y1, y2 = min(r1[1], r2[1]), max(r1[1], r2[1])
                for y in range(y1, y2+1):
                    cave[r1[0], y] = '#'
            else:
                # same Y
                x1, x2 = min(r1[0], r2[0]), max(r1[0], r2[0])
                for x in range(x1, x2+1):
                    cave[x, r1[1]] = '#'                
    
    bottom = max(c[1] for c in cave.keys())
    
    pos = SAND_SOURCE
    sand_count = 1
    part1 = None
    while True:
        if pos[1] == bottom:
            # bottom reached
            if part1 is None:
                part1 = sand_count - 1
        elif pos[1] == (bottom + 1):
            # bedrock reached
            cave[pos] = 'o'
            pos = SAND_SOURCE
            sand_count += 1
            continue

        down, left, right = (tuple(map(sum, zip(pos, m))) for m in MOVES)
        if cave[down] is None:
            # fall down
            pos = down
            continue
        elif cave[left] is None:
            # diagonal left
            pos = left
            continue
        elif cave[right] is None:
            # diagonal right
            pos = right
            continue
        else:
            cave[pos] = 'o'
            if pos[1] == 0:
                break
            pos = SAND_SOURCE
            sand_count += 1
            continue

    print("Part #1 :", part1)
    print("Part #2 :", sand_count)
