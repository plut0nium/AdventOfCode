#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from itertools import product
from functools import reduce

TILE_TRANSLATOR = str.maketrans({'.':'0','#':'1'})
BORDERS_DIRECTIONS = [(0,1),(1,0),(0,-1),(-1,0)]

class Tile:
    def __init__(self, a):
        self.array = np.array([list(map(int,t.translate(TILE_TRANSLATOR))) for t in a])
        self.rotation = 0
        self.flipped_x = False
        self.flipped_y = False
    
    def rotate(self, angle=90):
        self.rotation += angle
        self.rotation %= 360
    
    def flip_x(self):
        self.flipped_x = not self.flipped_x

    def flip_y(self):
        self.flipped_y = not self.flipped_y
        
    def get_array(self):
        r = np.rot90(self.array, self.rotation//90, axes=(1,0))
        if self.flipped_x:
            r = np.flip(r, 0)
        if self.flipped_y:
            r = np.flip(r, 1)
        return r
    
    def get_borders(self):
        r = self.get_array()
        return [''.join(map(str,b)) for b in (r[0,:], r[:,-1], r[-1,:], r[:,0]) ]
    
    def reset(self):
        self.rotation = 0
        self.flipped_x = False
        self.flipped_y = False


class Grid:
    def __init__(self, default=0):
        self.grid = {}
        self.default = default
        self.x_bound = [0, 0]
        self.y_bound = [0, 0]
    
    def set(self, x, y, value):
        self.grid[(x, y)] = value
        self.x_bound = (min(x, self.x_bound[0]),
                        max(x, self.x_bound[1]))
        self.y_bound = (min(y, self.y_bound[0]),
                        max(y, self.y_bound[1]))
    
    def get(self, x, y):
        return self.grid.get((x,y), self.default)
    
    def remove(self, x, y):
        if self.is_set(x, y):
            del self.grid[(x, y)]
    
    def is_set(self, x, y):
        return (x,y) in self.grid
    
    def is_in(self, x, y):
        return ((x >= self.x_bound[0] and x <= self.x_bound[1])
               and (y >= self.y_bound[0] and y <= self.y_bound[1]))
    
    def count(self, value):
        return list(self.grid.values()).count(value)
    
    def get_active_coords(self):
        return list(self.grid.keys())
    
    def get_size(self):
        return ((self.x_bound[1] - self.x_bound[0] + 1),
                (self.y_bound[1] - self.y_bound[0] + 1))
    
    def set_origin(self, x, y):
        grid_old = self.grid
        self.clear()
        for c, v in grid_old.items():
            x_new = c[0] - x
            y_new = c[1] - y
            self.set(x_new, y_new, v)
    
    def clear(self):
        self.grid = {}
        self.x_bound = [0, 0]
        self.y_bound = [0, 0]


input_file = "input"
input_file = "test1.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        image_raw = [i.strip().split('\n') for i in f.read().split('\n\n') if i.strip()]
    
    tiles = {}
        
    for i in image_raw:
        tile_id = int(i[0][5:9])
        tiles[tile_id] = Tile(i[1:])
        
    transformations = [t for t in product(range(4), range(2), range(2))]
    
    grid = Grid()
    to_place = list(tiles.keys())
    start = to_place.pop(0)
    grid.set(0, 0, start)
    
    while len(to_place):
        t = to_place.pop(0)
        if grid.count(t): # already in grid
            continue
        placed = False
        for r in transformations:
            tiles[t].reset()
            if r[0]:
                tiles[t].rotate(r[0]*90)
            if r[1]:
                tiles[t].flip_x()
            if r[2]:
                tiles[t].flip_y()
            borders = tiles[t].get_borders()
            for x,y in grid.get_active_coords():
                borders_p = tiles[grid.get(x,y)].get_borders()
                for d in range(4):
                    if borders_p[d] == borders[(d+2)%4]:
                        x_new, y_new = map(lambda a,b: a+b, (x,y), BORDERS_DIRECTIONS[d])
                        grid.set(x_new, y_new, t)
                        placed = True
                    if placed:
                        break
                if placed:
                    break
            if placed:
                break
        to_place.append(t) # not placed -> replace at the end of the queue
    
    count1 = reduce(lambda a,b: a*b, (grid.get(x,y) for x,y in product(grid.x_bound, grid.y_bound)))

    grid.set_origin(grid.x_bound[0], grid.y_bound[0])
    image_size = tuple(map(lambda a: a*8, grid.get_size()))
    image = np.zeros(image_size)
    for x,y in product(range(grid.x_bound[1]+1),
                       range(grid.y_bound[1]+1)):
        # TODO: correct cartesian coords x,y vs row,col in numpy...
        image[x*8:(x+1)*8,y*8:(y+1)*8] = tiles[grid.get(x,y)].get_array()[1:-1,1:-1]
        # DOES NOT WORK FOR NOW

    print("Step 1:", count1)
    print("Step 2:", count2)

