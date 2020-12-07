#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re

input_file = "input"
#input_file = "test1.txt"
#input_file = "test2.txt"

my_bag = "shiny gold"
bags = {}

bag_color_re = re.compile(r'^(\w+ \w+) bags contain')
contain_re = re.compile(r' (\d) (\w+ \w+) bag')

def can_contain_bag(b, c):
    if bags[b] is None: # b can not contain any other bag
        return False
    elif c in [x[1] for x in bags[b]]: # b can directly contain c
        return True
    else: # we need to go deeper
        return any(can_contain_bag(x, c) for x in [x[1] for x in bags[b]])

def count_inside(b):
    count = 0
    if bags[b] is None: # b can not contain any other bag
        pass
    else: # we need to go deeper
        for x in bags[b]:
            count += x[0] * (1 + count_inside(x[1]))
    return count

if __name__ == '__main__':
    count1, count2 = 0, 0
    
    with open(input_file,'r') as f:
        for l in [l.strip() for l in f.readlines() if len(l.strip())>0]:
            bag_color = bag_color_re.match(l).group(1)
            content = contain_re.findall(l)
            assert bag_color not in bags
            if len(content) == 0:
                bags[bag_color] = None
            else:
                bags[bag_color] = [(int(n),b) for n,b in content]

    # part 1
    for b in bags:
        if can_contain_bag(b, my_bag):
            count1 += 1

    # part 2
    count2 = count_inside(my_bag)

    print("Step 1:", count1)
    print("Step 2:", count2)


