#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math

input_file = "input"
#input_file = "test1.txt"

slopes = [(3, 1), (1, 1), (5, 1), (7, 1), (1, 2)]

with open(input_file,'r') as f:
    grid = [[c for c in l.strip()] for l in f.readlines()]

pattern_width = len(grid[0])

trees = []

for s in slopes:
    x,y = 0,0
    t = 0
    while True:
        x += s[0]
        x %= pattern_width
        y += s[1]
        if y >= len(grid): break
        if grid[y][x] == '#':
            t += 1
    trees.append(t)

#print(trees)
    
print("Step 1:", trees[0])
#print("Step 2:", np.prod(trees, dtype=np.int64))
print("Step 2:", math.prod(trees))

