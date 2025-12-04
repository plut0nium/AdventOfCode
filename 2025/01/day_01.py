#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test_01.txt"

DIAL_SIZE = 100

def part1(rotations, start=50):
    pos = [start]
    for r in rotations:
        pos.append((pos[-1] + r) % DIAL_SIZE)
    return pos.count(0)

def part2(rotations, start=50):
    pos = [start]
    zero_count = 0
    for r in rotations:
        next_pos = pos[-1] + r

        # >>> Does NOT work...        
        # if next_pos == 0:
        #     zero_count += 1
        # elif next_pos >= DIAL_SIZE:
        #     zero_count += next_pos // DIAL_SIZE
        # elif next_pos < 0:
        #     if pos[-1] == 0:
        #         zero_count += abs(r) // DIAL_SIZE
        #     else:
        #         zero_count += (abs(r) // DIAL_SIZE) + 1
        # else:
        #     pass

        
        if r < 0: # left
            zero_count += ((DIAL_SIZE - pos[-1]) % DIAL_SIZE + abs(r)) // DIAL_SIZE
        else:
            zero_count += (pos[-1] + r) // DIAL_SIZE

        pos.append(next_pos % DIAL_SIZE)
    return zero_count


if __name__ == '__main__':
    rotations = []
    with open(input_file, 'r') as f:
        for r in f.readlines():
            d = r[0]
            c = int(r[1:])
            rotations.append(c if d=="R" else -c)
    print(part1(rotations))
    print(part2(rotations))