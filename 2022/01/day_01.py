#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

if __name__ == '__main__':
    with open(input_file) as f:
        elves = [sum((int(c) for c  in e.split("\n")))
                   for e in f.read().strip().split("\n\n")]
    print("Part #1 :", max(elves))
    print("Part #2 :", sum(sorted(elves)[-3:]))
