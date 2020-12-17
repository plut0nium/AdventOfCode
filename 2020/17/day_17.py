#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product
from copy import deepcopy
from datetime import datetime
from operator import add

class Space:
    def __init__(self, n=3, default=0):
        self.n = n
        self.space = {}
        self.default = default
        self.extent = [(0,0)] * self.n
    
    def set(self, coords, value, allow_extend=False):
        c = self._check_coords(coords, allow_extend)
        self.space[c] = value
        for i in range(self.n):
            self.extent[i] = (min(c[i], self.extent[i][0]),
                              max(c[i], self.extent[i][1]))
    
    def get(self, coords):
        coords = self._check_coords(coords)
        return self.space.get(coords, self.default)
    
    def remove(self, coords):
        coords = self._check_coords(coords)
        if self.is_set(coords):
            del self.space[coords]
    
    def is_set(self, coords):
        coords = self._check_coords(coords)
        return coords in self.space
    
    def is_in(self, coords):
        coords = self._check_coords(coords)
        return all(coords[i] in range(self.extent[i][0],self.extent[i][1]+1) for i in range(self.n))
    
    def count(self, value):
        return list(self.space.values()).count(value)
    
    def add_dimension(self, n):
        space_old = self.space.copy()
        self.space = {}
        self.n += n
        self.extent = [(0,0)] * self.n
        for x in space_old.items():
            self.set(x[0], x[1], True)
    
    def get_active_coords(self):
        return list(self.space.keys())
    
    def _check_coords(self, coords, allow_extend=False):
        l = len(coords)
        if l == self.n:
            pass
        elif l < self.n:
            if allow_extend:
                coords = (coords) + (0,)*(self.n - l)
            else:
                raise ValueError('Not enough dimensions: {}, expected {}'.format(l, self.n))
        else:
            raise ValueError('Too many dimensions: {}, expected {}'.format(l, self.n))
        return coords

def conway_cubes(space, dimensions=3, loop=6):
    space = deepcopy(space)
    if space.n < dimensions:
        space.add_dimension(dimensions - space.n)
    directions = [d for d in product([-1,0,1], repeat=dimensions) if d != (0,)*dimensions]
    for i in range(loop):
        space_new = Space(dimensions)
        # space_new = deepcopy(space)
        # for c in product(*(range(e[0]-1,e[1]+2) for e in space.extent)):
        to_check = set()
        for x in space.get_active_coords():
            to_check.add(x)
            for d in directions:
                # to_check.add(tuple(x[i]+d[i] for i in range(dimensions)))
                to_check.add(tuple(map(add, x, d)))
        for c in to_check:
            n_active = 0
            for d in directions:
                # nc = tuple(c[i]+d[i] for i in range(dimensions))
                nc = tuple(map(add, c, d))
                if space.is_set(nc) and space.get(nc) == '#':
                    n_active += 1
            if space.is_set(c) and space.get(c) == '#':
                # if n_active not in (2,3):
                #     # space_new.set(c,'.')
                #     space_new.remove(c)
                if n_active in (2,3): # if new_space is empty (not a copy)
                    space_new.set(c, '#')
            else:
                if n_active == 3:
                    space_new.set(c, '#')
        space = space_new
    return space.count('#')


input_file = "input"
#input_file = "test1.txt"

if __name__ == '__main__':
    space = Space(2)
    x,y = 0,0

    with open(input_file,'r') as f:
        for r in [l.strip() for l in f.readlines() if l.strip()]:
            for c in r:
                if c == '#':
                    space.set((x,y), c)
                x += 1
            y+= 1
            x = 0

    # print("Step 1:", conway_cubes(space, 3))
    # print("Step 2:", conway_cubes(space, 4))

    # let's do some measurements...
    for n in range(2,6):
        start_time = datetime.now()
        print("n = {}:".format(n), conway_cubes(space, n), " -> ", datetime.now() - start_time)
