#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
# input_file = "test1.txt"
# input_file = "test2.txt"
# input_file = "test3.txt"

caves = defaultdict(set)

def pathfinder(cave, path, twice=False):
    if cave == "end":
        return [path + [cave]]
    if cave == "start" and len(path) != 0:
        return None
    if cave.islower() and cave in path:
        if twice:
            twice = False
        else:
            return None
    paths = []
    for route in caves[cave]:
        p = pathfinder(route,path + [cave],twice)
        if p is not None:
            paths += p
    return paths

if __name__ == '__main__':
    with open(input_file,'r') as f:
        for l in f.readlines():
            c1,c2 = l.strip().split("-")
            caves[c1].add(c2)
            caves[c2].add(c1)

    print(len(pathfinder("start", [])))
    print(len(pathfinder("start", [], True)))


