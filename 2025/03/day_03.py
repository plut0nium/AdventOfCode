#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test_01.txt"

from functools import reduce


def part1(banks):
    joltages = []
    for batteries in banks:
        b1 = max(batteries[:-1])
        b2 = max(batteries[batteries.index(b1)+1:])
        joltages.append(b1 * 10 + b2)
    return sum(joltages)


def part2(banks):
    joltages = []
    for batteries in banks:
        j = []
        k = 0 # index+1 of the last used battery
        for i in reversed(range(12)):
            batteries_available = batteries[k:-i] if i else batteries[k:]
            b = max(batteries_available)
            k += batteries_available.index(b) + 1
            j.append(b)
        joltages.append(reduce(lambda x, y: x * 10 + y, j))
    return sum(joltages)


if __name__ == '__main__':
    banks = []
    with open(input_file, 'r') as f:
        for l in f.readlines():
            banks.append(tuple(int(b) for b in l.strip()))

    print(part1(banks))
    print(part2(banks))