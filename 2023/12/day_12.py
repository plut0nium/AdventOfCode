#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
input_file = "test01.txt"
# input_file = "test02.txt"

OPERATIONNAL = "."
DAMAGED = "#"
UNKNOWN = "?"

def parse_springs(springs_lines):
    springs = []
    for l in springs_lines:
        s, c = l.strip().split()
        c = [int(v) for v in c.split(",")]
        springs.append((s,c))
    return springs

def check_arrangements(spring):
    # create a minimal arrangement of blanks
    blanks = [1 for _ in range(len(springs[1]) - 1)]
    if spring[0].startswith(UNKNOWN):
        blanks.insert(0, 0) # insert
    elif spring[0].startswith(OPERATIONNAL):
        blanks.insert(0, 1)
    if spring[0].endswith(UNKNOWN):
        blanks.append(0)
    elif spring[0].endswith(OPERATIONNAL):
        blanks.append(1)
    remaining_blanks = len(spring[0]) - sum(spring[1]) - sum(blanks)
    print(*spring, blanks, remaining_blanks)
    return None

def part1(springs):
    for s in springs:
        check_arrangements(s)
    return None

def part2(springs):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        springs = parse_springs(f.readlines())
    print("Part #1 :", part1(springs))
    print("Part #2 :", part2(springs))
