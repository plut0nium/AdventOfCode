#!/usr/bin/env python
# -*- coding: utf-8 -*-

from operator import add,mul
from copy import copy

operators = {'+': add, '*': mul, }

def operation_order(expr, advanced=False):
    op_stack = []
    while len(expr) > 0:
        o = expr.pop(0)
        if o == '(':
            res, expr = operation_order(expr, advanced)
            op_stack.append(res)
        elif o == ')':
            break
        else:
            op_stack.append(o)
        if len(op_stack) > 1 and len(op_stack) % 2 == 1:
            if not advanced or op_stack[-2] == '+':
                # in normal mode evaluate everything
                # in advanced mode, only evaluate additions first
                a, x, b = op_stack[-3:]
                op_stack = op_stack[:-3]
                op_stack.append(operators[x](int(a),int(b)))
    if len(op_stack) > 1:
        # only remaining operations should be multiplications
        res, _ = operation_order(op_stack)
    else:
        res = op_stack[0]
    return res, expr
    

input_file = "input"
test_input = None
# test_input = ["1 + 2 * 3 + 4 * 5 + 6",
#               "1 + (2 * 3) + (4 * (5 + 6))",
#               "2 * 3 + (4 * 5)",
#               "5 + (8 * 3 + 9 + 3 * 4 * 3)",
#               "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))",
#               "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

if __name__ == '__main__':
    count1, count2 = 0, 0

    if test_input is None:
        with open(input_file,'r') as f:
            lines = [l.strip() for l in f.readlines() if l.strip()]
    else:
        lines = test_input

    for l in lines:
        l = l.replace('(', '( ').replace(')', ' )') # add spaces around parentheses
        expr = l.split(' ')
        # part 1
        r, _ = operation_order(copy(expr))
        count1 += r
        # part 2
        r2, _ = operation_order(expr, True)
        count2 += r2

    print("Step 1:", count1)
    print("Step 2:", count2)

