#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from math import prod
from itertools import product

OPERATORS = ["+", "*"]

def part1(equations):
    valid = []
    for e in equations:
        value = e[0]
        numbers = e[1]
        for operators in product(OPERATORS, repeat=(len(numbers) - 1)):
            result = numbers[0]
            for i, o in enumerate(operators):
                if o == "+":
                    result += numbers[i+1]
                elif o == "*":
                    result *= numbers[i+1]
                else:
                    raise ValueError(f"Unknown operator: {o}")
            if result == value:
                valid.append(value)
                break
    return sum(valid)


def part2(equations):
    return None

if __name__ == '__main__':
    equations = []
    with open(input_file, 'r') as f:
        for e_str in f.readlines():
            value, num_str = e_str.split(": ")
            numbers = tuple(map(int, num_str.strip().split(" ")))
            equations.append((int(value), numbers))
    print(part1(equations))
    print(part2(equations))
