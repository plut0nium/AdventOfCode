#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from collections import defaultdict
from itertools import product

input_file = "input"
#input_file = "test1.txt"
#input_file = "test2.txt"

#re_prog = re.compile(r'(?:^(mask) = ([X01]{36}))|(?:^(mem)\[(\d+)\] = (\d+))')
re_prog = re.compile(r'^(mask|mem)\[?(\d*)\]? = ([X01]{36}|\d+)')


if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        program = [re_prog.match(l.strip()).groups() for l in f.readlines() if l.strip()]

    mem1 = defaultdict(int)
    mem2 = defaultdict(int)

    for l in program:
        if l[0] == 'mask':
            mask_set = 0
            mask_clear = 0
            floating = []
            for b,v in enumerate(reversed(l[2])):
                if v == '1':
                    mask_set |= 1 << b
                elif v == '0':
                    mask_clear |= 1 << b
                else: # 'X'
                    floating.append(b)
        else:
            # part 1
            mem1[int(l[1])] = (int(l[2]) | mask_set) & ~mask_clear
            # part 2
            for p in product(range(2), repeat=len(floating)):
                addr = int(l[1]) | mask_set
                for i, b in enumerate(reversed(floating)):
                    if p[i] == 0:
                        addr &= ~(1 << b)
                    else:
                        addr |= 1 << b
                mem2[addr] = int(l[2])

    count1 = sum(v for _, v in mem1.items())
    count2 = sum(v for _, v in mem2.items())

    print("Step 1:", count1)
    print("Step 2:", count2)


