#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
input_file = "test02.txt"
# input_file = "test03.txt"

from collections import defaultdict
from itertools import chain
import re

digit_re = re.compile(r'\d+')


def run(program, registers):
    ip = 0
    output = []
    while True:
        if ip >= len(program):
            break
        opcode = program[ip]
        operand = program[ip+1]
        # operand
        if 0 <= operand <= 3:
            operand_value = operand
        elif 4 <= operand <= 6:
            operand_value = registers[operand - 4]
        else:
            operand_value = None
            # raise ValueError(f"Unsupported operand: {operand}")
        # program
        if opcode == 0: # adv
            registers[0] = int(registers[0] / (2.0 ** operand_value))
        elif opcode == 1: # bxl
            registers[1] = registers[1] ^ operand
        elif opcode == 2: # bst
            registers[1] = operand_value % 8
        elif opcode == 3: # jnz
            if registers[0] != 0:
                ip = operand
                continue
        elif opcode == 4: # bxc
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5: # out
            output.append(operand_value % 8)
        elif opcode == 6: # bdv
            registers[1] = int(registers[0] / (2.0 ** operand_value))
        elif opcode == 7: # cdv
            registers[2] = int(registers[0] / (2.0 ** operand_value))
        else:
            raise ValueError(f"Unsupported opcode: {opcode}")
        ip += 2
    return output


def part1(program, registers):
    return ",".join(str(v) for v in run(program, registers))


def part2(program, registers):
    return ",".join(str(v) for v in run(program, registers))


def part2_brute(program, registers):
    register_a = 0
    while True:
        registers = [register_a, 0, 0]
        output = run(program, registers)
        if len(output) == len(program) \
            and all(a == b for a,b in zip(output, program)):
            return register_a
        register_a += 1
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        r, p = f.read().split("\n\n")
        registers = [int(d) for d in digit_re.findall(r)]
        program = [int(o) for o in p.split(":")[1].strip().split(",")]
    print(part1(program, registers))
    print(part2_brute(program, registers))
