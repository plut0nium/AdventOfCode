#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

elves = []

if __name__ == '__main__':
    elves.append(0)
    for l in open(input_file).readlines():
        l = l.strip()
        if len(l):
            elves[-1] += int(l)
        else:
            elves.append(0)
    print("Part #1 :", max(elves))
    print("Part #2 :", sum(sorted(elves)[-3:]))
