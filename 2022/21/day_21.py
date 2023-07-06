#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
from scipy.optimize import root_scalar

input_file = "input"
# input_file = "test01.txt"

def monkey_math(m, monkeys):
    if isinstance(monkeys[m], int) or isinstance(monkeys[m], float):
        return monkeys[m]
    m1, op, m2 = monkeys[m]
    if op == '+':
        return monkey_math(m1, monkeys) + monkey_math(m2, monkeys)
    elif op == '-':
        return monkey_math(m1, monkeys) - monkey_math(m2, monkeys)
    elif op == '*':
        return monkey_math(m1, monkeys) * monkey_math(m2, monkeys)
    elif op == '/':
        return monkey_math(m1, monkeys) / monkey_math(m2, monkeys)
    else:
        raise ValueError

def monkey_math2(monkeys):
    def f(x, monkeys):
        m1, _, m2 = monkeys['root']
        v2 = monkey_math(m2, monkeys)
        monkeys['humn'] = x
        return monkey_math(m1, monkeys) - v2
    
    sol = root_scalar(f, args=(monkeys), x0=8_000_000, x1=23_622_695_042_414)
    if sol.converged == True:
        return sol.root
    return None


if __name__ == '__main__':
    start_time = time()
    monkeys = {}
    for m in open(input_file, 'r').readlines():
        n, v = m.strip().split(': ')
        try:
            v = int(v)
        except ValueError:
            v = v.split()
        monkeys[n] = v

    print("Part #1 :", monkey_math('root', monkeys))
    
    print("Part #2 :", monkey_math2(monkeys))
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
