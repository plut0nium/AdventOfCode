#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from itertools import product
from copy import deepcopy

input_file = "input"
#input_file = "test1.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0

    space = {}
    x,y,z,w = 0,0,0,0
    xmin, xmax = 0,0
    ymin, ymax = 0,0
    zmin, zmax = 0,0
    wmin, wmax = 0,0

    with open(input_file,'r') as f:
        for r in [l.strip() for l in f.readlines() if l.strip()]:
            ymax = y
            for c in r:
                xmax = x
                space[(x,y,z)] = c
                x += 1
            y+= 1
            x = 0
    
    initial_space = deepcopy(space)
    directions = [d for d in product([-1,0,1], repeat=3) if d != (0,0,0)]

    for i in range(6):
        space_new = deepcopy(space)
        for x in range(xmin-1, xmax+2):
            for y in range(ymin-1, ymax+2):
                for z in range(zmin-1, zmax+2):
                    n_active = 0
                    for d in directions:
                        nx = x + d[0]
                        ny = y + d[1]
                        nz = z + d[2]
                        if (nx,ny,nz) in space and space[(nx,ny,nz)] == '#':
                            n_active += 1
                    # print(x,y,z," - ",n_active)
                    if (x,y,z) in space and space[(x,y,z)] == '#':
                        if n_active in (2,3):
                            pass
                        else:
                            space_new[(x,y,z)] = '.'
                    else:
                        if n_active == 3:
                            space_new[(x,y,z)] = '#'
                            xmin = min(x,xmin)
                            xmax = max(x,xmax)
                            ymin = min(y,ymin)
                            ymax = max(y,ymax)
                            zmin = min(z,zmin)
                            zmax = max(z,zmax)
        space = space_new

    count1 = list(space.values()).count('#')

    # part 2
    directions = [d for d in product([-1,0,1], repeat=4) if d != (0,0,0,0)]
    
    space = {}
    for c in initial_space.items():
        coords = tuple(list(c[0])+[0])
        space[coords] = c[1]

    for i in range(6):
        space_new = deepcopy(space)
        for x in range(xmin-1, xmax+2):
            for y in range(ymin-1, ymax+2):
                for z in range(zmin-1, zmax+2):
                    for w in range(wmin-1,wmax+2):
                        n_active = 0
                        for d in directions:
                            nx = x + d[0]
                            ny = y + d[1]
                            nz = z + d[2]
                            nw = w + d[3]
                            if (nx,ny,nz,nw) in space and space[(nx,ny,nz,nw)] == '#':
                                n_active += 1
                        # print(x,y,z," - ",n_active)
                        if (x,y,z,w) in space and space[(x,y,z,w)] == '#':
                            if n_active in (2,3):
                                pass
                            else:
                                space_new[(x,y,z,w)] = '.'
                        else:
                            if n_active == 3:
                                space_new[(x,y,z,w)] = '#'
                                xmin = min(x,xmin)
                                xmax = max(x,xmax)
                                ymin = min(y,ymin)
                                ymax = max(y,ymax)
                                zmin = min(z,zmin)
                                zmax = max(z,zmax)
                                wmin = min(w,wmin)
                                wmax = max(w,wmax)
        space = space_new

    count2 = list(space.values()).count('#')

    print("Step 1:", count1)
    print("Step 2:", count2)
