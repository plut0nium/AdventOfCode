# -*- coding: utf-8 -*-

import numpy as np

coords = [tuple(map(int, line.strip().split(","))) for line in open('input.txt')]

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# PART 1

def closest(a):
    d = [dist(a,c) for c in coords]
    d_min = min(d)
    if d.count(d_min) > 1:
        return -1
    return d.index(d_min)

domain = np.zeros((400,400), dtype=int)

it = np.nditer(domain, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    it[0] = closest(it.multi_index)
    it.iternext()

inner_domain = set(range(len(coords))).difference(
                                    np.unique(np.concatenate((domain[:,0],
                                                              domain[:,-1],
                                                              domain[0,:],
                                                              domain[-1,:]))))

print(max([np.count_nonzero(domain == x) for x in inner_domain]))

# PART 2

domain2 = np.zeros((400,400), dtype=int)
it = np.nditer(domain2, flags=['multi_index'], op_flags=['readwrite'])
while not it.finished:
    it[0] = sum([dist(it.multi_index,c) for c in coords])
    it.iternext()

print(np.count_nonzero(domain2 < 1e4))
