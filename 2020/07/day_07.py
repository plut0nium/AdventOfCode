#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re

#input_file = "input"
input_file = "test1.txt"

my_bag = "shiny gold"

bag_re = re.compile(r'^(\w+ \w+) bags contain')

if __name__ == '__main__':
    count1, count2 = 0, 0
    
    with open(input_file,'r') as f:
        data = [l.strip() for l in f.readlines() if len(l.strip())>0]

    print(data)

    print("Step 1:", count1)
    print("Step 2:", count2)


