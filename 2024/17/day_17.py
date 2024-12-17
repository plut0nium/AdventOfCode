#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"

import re
import sys

sys.path.append("..")
from utils import timing

digit_re = re.compile(r'\d+')


def combo(operand, registers):
    # operand
    if 0 <= operand <= 3:
        return operand
    elif 4 <= operand <= 6:
        return registers[operand - 4]
    else:
        raise ValueError(f"Unsupported combo operand: {operand}")
    return None


def run(program, registers):
    ip = 0
    output = []
    while True:
        if ip >= len(program):
            break
        opcode = program[ip]
        operand = program[ip+1]
        # program
        if opcode == 0: # adv
            registers[0] = registers[0] // (2 ** combo(operand, registers))
        elif opcode == 1: # bxl
            registers[1] = registers[1] ^ operand
        elif opcode == 2: # bst
            registers[1] = combo(operand, registers) % 8
        elif opcode == 3: # jnz
            if registers[0] != 0:
                ip = operand
                continue
        elif opcode == 4: # bxc
            registers[1] = registers[1] ^ registers[2]
        elif opcode == 5: # out
            output.append(combo(operand, registers) % 8)
        elif opcode == 6: # bdv
            registers[1] = registers[0] // (2 ** combo(operand, registers))
        elif opcode == 7: # cdv
            registers[2] = registers[0] // (2 ** combo(operand, registers))
        else:
            raise ValueError(f"Unsupported opcode: {opcode}")
        ip += 2
    return output


@timing
def part1(program, registers):
    return ",".join(str(v) for v in run(program, registers))


@timing
def part2(program):
    queue = [(1, 0)]
    while len(queue):
        nb_digits, register_a = queue.pop(0)
        for i in range(8):
            register_a_new = (register_a << 3) + i # assumes all programs have adv(3)
            result = run(program, [register_a_new, 0, 0])
            if result == program[len(program) - nb_digits:]:
                # got the last nb_digits right
                if len(program) == nb_digits:
                    # all digits right !
                    return register_a_new
                queue.append((nb_digits + 1, register_a_new))
    return None


def part2_brute(program, registers):
    register_a = registers[0]
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
    print(part1(program, registers[:]))
    print(part2(program))
