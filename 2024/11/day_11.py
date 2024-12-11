#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from collections import defaultdict, Counter


def blink(stones):
    stones2 = []
    for s in stones:
        if s == 0:
            stones2.append(1)
        elif not (len(s2 := str(s)) % 2):
            # even number of digits
            a, b = map(int, (s2[:len(s2)//2], s2[len(s2)//2:]))
            stones2.extend((a,b))
        else:
            stones2.append(s * 2024)
    return stones2


def blink2(stones):
    # count stones
    stones2 = Counter()
    for s in stones.keys():
        if s == 0:
            stones2[1] += stones[s]
        elif not (len(s2 := str(s)) % 2):
            # even number of digits
            a, b = map(int, (s2[:len(s2)//2], s2[len(s2)//2:]))
            stones2[a] += stones[s]
            stones2[b] += stones[s]
        else:
            stones2[s * 2024] += stones[s]    
    return stones2


def part1(stones, repeat=25):
    stones = stones[:] # make a copy
    for i in range(repeat):
        stones = blink(stones)
    return len(stones)


def part2(stones, repeat=75):
    stones_counter = Counter(stones)
    for i in range(repeat):
        stones_counter = blink2(stones_counter)
    return stones_counter.total()


if __name__ == '__main__':
    stones = []
    with open(input_file, 'r') as f:
        for s in f.read().strip().split(" "):
            stones.append(int(s))
    print(part1(stones))
    print(part2(stones))
