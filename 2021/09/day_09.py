#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

input_file = "input"
#input_file = "test1.txt"

directions = [(-1,0),(1,0),(0,-1),(0,1)]

if __name__ == '__main__':
    heightmap = []
    low_points = []
    
    with open(input_file,'r') as f:
        for l in f.readlines():
            heightmap.append([9]+[int(h) for h in l.strip()]+[9])
        heightmap.insert(0, [9 for _ in heightmap[-1]])
        heightmap.append([9 for _ in heightmap[-1]])
    
    for i in range(1, len(heightmap)-1):
        for j in range(1, len(heightmap[i])-1):
            adj = [tuple(sum(v) for v in zip((i,j),d)) for d in directions]
            if heightmap[i][j] == 9:
                continue
            if all(heightmap[x][y] > heightmap[i][j] for (x,y) in adj):
                low_points.append((i,j))
    print(sum(heightmap[i][j] + 1 for i,j in low_points))
    
    basins = []
    for p in low_points:
        basin = set()
        candidates = [tuple(sum(v) for v in zip(p,d)) for d in directions]
        while len(candidates):
            x,y = candidates.pop()
            if heightmap[x][y] < 9:
                basin.add((x,y))
                for d in [tuple(sum(v) for v in zip((x,y),d)) for d in directions]:
                    if d not in basin:
                        candidates.append(d)
                    else:
                        pass
        basins.append(basin)

    print(math.prod(sorted(len(b) for b in basins)[-3:]))