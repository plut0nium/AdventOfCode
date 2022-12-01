#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import time
import numpy as np
import heapq as hq

input_file = "input"
input_file = "test1.txt"

start = (0,0)
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def search(m):
    h,w = len(m), len(m[0])
    seen = [[None for _ in range(w)] for _ in range(h)]
    q = [(0,start)]     # risk, starting point
    while q:
        risk, (x,y) = hq.heappop(q)
        if (x,y) == (w-1,h-1):
            return risk
        for x,y in [(x+d[0],y+d[1]) for d in directions]:
            if x >= 0 and x < w and y >= 0 and y < h and not seen[y][x]:
                hq.heappush(q, (risk+(m[y][x] % 9)+1, (x,y)))
                seen[y][x] = 1    # mark as seen

if __name__ == '__main__':
    with open(input_file,'r') as f:
        grid = [[int(c)-1 for c in r.strip()] for r in f.readlines()]
    print(search(grid))
    m = np.array(grid)
    m = np.concatenate([m+i for i in range(5)], axis=0)
    m = np.concatenate([m+i for i in range(5)], axis=1)
    print(search(m))

    
