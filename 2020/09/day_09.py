#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re
from itertools import combinations

input_file = "input"
# input_file = "test1.txt"

preamble_size = 25
# preamble_size = 5


if __name__ == '__main__':
    count1, count2 = 0, 0
    
    with open(input_file,'r') as f:
        data = [int(l.strip()) for l in f.readlines() if len(l.strip())>0]

    # part 1
    for i in range(preamble_size, len(data)):
        if data[i] not in [sum(c) for c in combinations(data[i-preamble_size:i], 2)]:
            count1 = data[i]
            break
    
    # part 2
    for j in range(2, len(data)):
        for k in range(len(data)-j):
            if sum(data[k:k+j]) == count1:
                count2 = min(data[k:k+j]) + max(data[k:k+j])
                break
        if count2 != 0:
            break

    print("Step 1:", count1)
    print("Step 2:", count2)


