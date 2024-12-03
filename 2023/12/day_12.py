#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

OPERATIONNAL = "."
DAMAGED = "#"
UNKNOWN = "?"

from functools import cache

def parse_springs(springs_lines):
    springs = []
    for l in springs_lines:
        s, c = l.strip().split()
        c = tuple(int(v) for v in c.split(","))
        springs.append((s,c))
    return springs

@cache
def check_arrangements(springs, groups, current_group_size=0):
    # print(springs, groups, current_group_size)
    # group started if size > 0
    
    if len(springs) == 0 or all(s == OPERATIONNAL for s in springs):
        # no spring left, or all remaining springs are OP
        if current_group_size > 0:
            # group started and size is correct -> 1
            return int(len(groups) == 1 and current_group_size == groups[0])
        else:
            # no group started and no group left -> 1
            return int(len(groups) == 0)

    if current_group_size > 0:
        # group started
        if not groups or current_group_size > groups[0]:
            # ...but size is too high
            # or no group left
            return 0

    if springs[0] == OPERATIONNAL:
        if current_group_size > 0:
            # group started -> close it
            if current_group_size != groups[0]:
                # if size not correct -> 0
                return 0
            else:
                # size correct -> go to next group
                groups = groups[1:]
        else:
            # no group started, do nothing
            pass
        return check_arrangements(springs[1:], groups, 0)
    elif springs[0] == DAMAGED:
        # increase group size
        return check_arrangements(springs[1:], groups, current_group_size+1)
    else: # UNKNOWN-> can be either OPERATIONNAL or DAMAGED
        if not groups or current_group_size == groups[0]:
            # current group size is correct -> close it
            # or no group left
            # ---> this spring must be OPERATIONNAL
            return check_arrangements(springs[1:], groups[1:], 0)
        elif current_group_size > 0:
            # if a group is started and current size is not exceeded
            # ---> this spring can be DAMAGED
            return check_arrangements(springs[1:], groups, current_group_size+1)
        else: # group size == 0
            # no group started yet
            # check both options (start group, or not)
            return check_arrangements(springs[1:], groups, 1) \
                    + check_arrangements(springs[1:], groups, 0)

def unfold(s, count = 5):
    springs = UNKNOWN.join([s[0]] * count)
    groups = s[1] * count
    return springs, groups

def part1(springs):
    arrangements = [check_arrangements(*s) for s in springs]
    return sum(arrangements)

def part2(springs):
    arrangements = [check_arrangements(*unfold(s)) for s in springs]
    return sum(arrangements)


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        springs = parse_springs(f.readlines())
    print("Part #1 :", part1(springs))
    print("Part #2 :", part2(springs))
