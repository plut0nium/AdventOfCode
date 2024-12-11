#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"


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


def part1(stones):
    stones = stones[:] # make a copy
    for i in range(25):
        stones = blink(stones)
    return len(stones)


def part2(stones):

    return len(stones)



if __name__ == '__main__':
    stones = []
    with open(input_file, 'r') as f:
        for s in f.read().strip().split(" "):
            stones.append(int(s))
    print(part1(stones))
    print(part2(stones))
