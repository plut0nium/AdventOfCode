#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from functools import cache

def parse_sequence(input_lines):
    sequence = "".join(l.strip() for l in input_lines).split(",")
    return sequence

@cache
def HASH(str):
    # Holiday ASCII String Helper algorithm
    h = 0
    for c in str:
        h += ord(c)
        h *= 17
        h %= 256
    return h

@timing
def part1(sequence):
    return sum(HASH(s) for s in sequence)

@timing
def part2(sequence):
    boxes = [{} for _ in range(256)]
    for s in sequence:
        focal_length = None
        if s.endswith("-"):
            label = s[:-1]
        else:
            label = s[:-2]
            focal_length = int(s[-1])
        box_idx = HASH(label)
        if focal_length is None:
            if label in boxes[box_idx]:
                boxes[box_idx].pop(label)
        else:
                boxes[box_idx][label] = focal_length
    focusing_power = 0
    for i, b in enumerate(boxes):
        if len(b):
            for j, l in enumerate(b):
                focusing_power += (i + 1) * (j + 1) * b[l]
    return focusing_power


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        init_sequence = parse_sequence(f.readlines())
    print("Part #1 :", part1(init_sequence))
    print("Part #2 :", part2(init_sequence))
