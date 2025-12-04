#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test_01.txt"


from math import log10
from itertools import batched


def part1(ranges):
    c = 0
    for r in ranges:
        lo, hi = r
        for i in range(lo, hi + 1):
            if int(log10(i)) % 2: # odd number of digits
                i_str = str(i)
                l = len(i_str) // 2
                if i_str[:l] == i_str[l:]:
                    c += i
    return c


def part2(ranges):
    invalid = set()
    for r in ranges:
        lo, hi = r
        for i in range(lo, hi + 1):
            i_str = str(i)
            for l in range(1, len(i_str) // 2 + 1):
                if len(set(batched(i_str, l))) == 1:
                    invalid.add(i)
                    break
    return sum(invalid)


if __name__ == '__main__':
    ranges = []
    with open(input_file, 'r') as f:
        for r in f.readline().split(","):
            ranges.append(tuple(map(int, r.split('-'))))

    print(part1(ranges))
    print(part2(ranges))