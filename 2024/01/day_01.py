#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"

import re

def part1(l1, l2):
    assert(len(l1) == len(l2))
    l1.sort()
    l2.sort()
    return sum(abs(l1[i] - l2[i]) for i in range(len(l1)))


def part2(l1, l2):
    similarity = 0
    for i in l1:
        similarity += l2.count(i) * i
    return similarity


if __name__ == '__main__':
    l1 = []
    l2 = []
    for l in open(input_file, 'r').readlines():
        l,r = map(int, re.split(r'[ ]+',l.strip()))
        l1.append(l)
        l2.append(r)
    print(part1(l1, l2))
    print(part2(l1, l2))
