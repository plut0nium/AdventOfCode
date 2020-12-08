#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re

from copy import deepcopy

input_file = "input"
#input_file = "test1.txt"

def run(code):
    accumulator = 0
    iptr = 0
    # progam_sequence = []
    progam_sequence = set()
    exit_status = 0
    end = False
    while True:
        if iptr == len(code)-1:
            end = True
        if code[iptr][0] == 'nop':
            iptr += 1
        elif code[iptr][0] == 'acc':
            accumulator += code[iptr][1]
            iptr += 1
        elif code[iptr][0] == 'jmp':
            iptr += code[iptr][1]
        else:
            # error
            pass
        if iptr not in progam_sequence:
            # progam_sequence.append(iptr)
            progam_sequence.add(iptr)
        else: # loop detected
            exit_status = 1
            end = True
        if end:
            break
    return accumulator, exit_status

if __name__ == '__main__':
    count1, count2 = 0, 0
    
    code = []
    with open(input_file,'r') as f:
        for l in f.readlines():
            if len(l.strip()) == 0:
                continue
            ins, arg = l.strip().split(' ')
            code.append((ins, int(arg)))

    # part 1
    count1, _ = run(code)
    
    # part 2
    instruction_replace = {'jmp':'nop', 'nop':'jmp'}
    for i in range(len(code)):
        if code[i][0] in instruction_replace:
            test_code = deepcopy(code)
            test_code[i] = (instruction_replace[test_code[i][0]], test_code[i][1])
            count2, status = run(test_code)
            if status == 0: # program exited normally
                break

    print("Step 1:", count1)
    print("Step 2:", count2)


