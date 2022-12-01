#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test1.txt"

grid = defaultdict(int)
grid2 = defaultdict(int) # for part 2

with open(input_file,'r') as f:
    for s in f.readlines():
        p1, p2 = s.split(" -> ")
        x1,y1 = map(int,p1.split(","))
        x2,y2 = map(int,p2.split(","))
        if x1 == x2:
            for y in range(min(y1,y2),max(y1,y2)+1):
                grid[(x1,y)] += 1
        elif y1 == y2:
            for x in range(min(x1,x2),max(x1,x2)+1):
                grid[(x,y1)] += 1
        else:
            dx = x2 - x1
            dy = y2 - y1
            if dx * dy > 0:
                if dx > 0:
                    for i in range(dx+1):
                        grid2[x1+i,y1+i] += 1
                else: # dx = dy  < 0
                    for i in range(-dx+1):
                        grid2[x2+i,y2+i] += 1
            else: # dx = -dy
                if dx > 0: # dy < 0
                    for i in range(dx+1):
                        grid2[x1+i,y1-i] += 1
                else:
                    for i in range(dy+1):
                        grid2[x1-i,y1+i] += 1                  

for k in grid.keys(): # merge grid 1 in 2
    grid2[k] += grid[k]

print(len([p for p in grid.values() if p > 1]))
print(len([p for p in grid2.values() if p > 1]))