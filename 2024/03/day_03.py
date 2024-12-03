#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

import re

mul_re = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')


def part1(program):
    return run(program)


def part2(program):
    return run(program, part2=True)


def run(program, part2=False):
    result = 0
    enabled = True
    valid = mul_re.findall(program)
    for v in valid:
        if v == "do()":
            enabled = True
        elif v == "don't()":
            enabled = False
        else:
            if enabled or not part2:
                # could get x,y directly from the regex...
                x, y = list(map(int, v[4:-1].split(',')))
                result += x * y
    return result


if __name__ == '__main__':
    with open(input_file, 'r') as file:
        program = file.read()
    print(part1(program))
    print(part2(program))
