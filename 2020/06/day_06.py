#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re

input_file = "input"
#input_file = "test1.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0
    
    with open(input_file,'r') as f:
        for g in f.read().strip().split('\n\n'):
            # part 1
            g1 = g.replace('\n','')
            # answers = set()
            # for a in g1:
            #     answers.add(a)
            # count1 += len(answers)
            count1 += len(set(g1))
            # part 2
            g2 = g.split('\n')
            for a in g2[0]: # only check for answers of 1st member
                if all(a in x for x in g2):
                    count2 += 1

    print("Step 1:", count1)
    print("Step 2:", count2)


