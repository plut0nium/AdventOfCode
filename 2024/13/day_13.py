#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


from collections import defaultdict, Counter
import re
import numpy as np

machine_regex = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\n'
                          +r'Button B: X\+(\d+), Y\+(\d+)\n'
                          +r'Prize: X=(\d+), Y=(\d+)')
TARGET_OFFSET = 10000000000000


def solve_machine(A, B, prize, offset=0):
    a = np.array([A, B]).transpose()
    b = np.array(prize) + offset
    solution = np.around(np.linalg.solve(a, b), 3)
    if all(x.is_integer() for x in solution):
        return tuple(map(int, solution))
    return None


def part1(machines):
    token_count = 0
    for m in machines:
        solution = solve_machine(*m)
        if solution:
            token_count += 3 * solution[0] + 1 * solution[1]
    return token_count


def part2(machines):
    token_count = 0
    for m in machines:
        solution = solve_machine(*m, TARGET_OFFSET)
        if solution:
            token_count += 3 * solution[0] + 1 * solution[1]
    return token_count


if __name__ == '__main__':
    machines = []
    with open(input_file, 'r') as f:
        for m in f.read().split("\n\n"):
            ax, ay, bx, by, tx, ty = map(int, machine_regex.match(m).groups())
            machines.append(((ax, ay), (bx, by), (tx, ty)))
    print(part1(machines))
    print(part2(machines))
