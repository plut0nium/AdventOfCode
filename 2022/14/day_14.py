#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict, Counter

input_file = "input"
#input_file = "test01.txt"

SAND_SOURCE = (500,0)
MOVES = [(0,1), (-1,1), (1,1)]

class CaveOverFlowError(Exception):
    pass

class Cave(defaultdict):
    def __init__(self, *args, **kwargs):
        super().__init__(lambda: None, *args, **kwargs)
        self.lowest = 0

    def add_scan(self, s):
        for i in range(1,len(s)):
            s1 = s[i-1]
            s2 = s[i]
            if s1[0] == s2[0]:
                # same X
                y1, y2 = min(s1[1], s2[1]), max(s1[1], s2[1])
                for y in range(y1, y2+1):
                    self[s1[0], y] = '#'
            else:
                # same Y
                x1, x2 = min(s1[0], s2[0]), max(s1[0], s2[0])
                for x in range(x1, x2+1):
                    self[x, s1[1]] = '#'
            self.lowest = max(s1[1], s2[1], self.lowest)
    
    def pour_sand(self, source):
        # return the position where sand settles
        # raise an exception if cave is full
        if self[source] == 'o':
            raise CaveOverFlowError
        pos = source
        while True:
            if pos[1] == (self.lowest + 1):
                # "virtual" bedrock reached
                self[pos] = 'o'
                return pos
    
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
                return pos
        # we should not be here
        return None
    
    def count_sand(self):
        return Counter(self.values())['o']

if __name__ == '__main__':
    cave = Cave()
    for l in open(input_file, 'r').readlines():
        s = [tuple(map(int, c.split(','))) for c in l.strip().split(' -> ')]
        cave.add_scan(s)
    
    part1 = None
    while True:
        try:
            p = cave.pour_sand(SAND_SOURCE)
            if part1 is None and p[1] >= cave.lowest:
                part1 = cave.count_sand() - 1
        except CaveOverFlowError:
            break

    print("Part #1 :", part1)
    print("Part #2 :", cave.count_sand())
