#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import product

input_file = "input"
#input_file = "test1.txt"

steps = 100

if __name__ == '__main__':
    
    with open(input_file,'r') as f:
        octopus = [[int(o) for o in l.strip()] for l in f.readlines()]

    X, Y = len(octopus), len(octopus[0])

    flashed = []
    while True:
        flashed.append(set())
        for i in range(X):
            for j in range(Y):
                octopus[i][j] += 1
        while any((o > 9 and o < 99) for r in octopus for o in r):
            for i in range(X):
                for j in range(Y):
                    if octopus[i][j] > 9 and (i,j) not in flashed[-1]:
                        flashed[-1].add((i,j))
                        octopus[i][j] += 100 # make sure it will not trigger again
                        for k,l in product(range(i-1,i+2),range(j-1,j+2)):
                            # this also increment i,j but we don't care here
                            if k < 0 or k >= X:
                                continue
                            if l < 0 or l >= Y:
                                continue
                            octopus[k][l] += 1
        for i,j in flashed[-1]:
            octopus[i][j] = 0
        if len(flashed[-1]) == X*Y: # all octopuses flash simultaneously !
            break
    
    print(sum(len(f) for f in flashed[:steps]))
    print(len(flashed))
    