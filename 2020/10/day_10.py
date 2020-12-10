#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

input_file = "input"
# input_file = "test1.txt"
# input_file = "test2.txt"

outlet_joltage = 0

if __name__ == '__main__':
    count1, count2 = 0, 0
    
    with open(input_file,'r') as f:
        data = [int(l.strip()) for l in f.readlines() if len(l.strip())>0]

    buit_in_joltage = max(data) + 3
    data.extend([outlet_joltage, buit_in_joltage])
    data.sort()

    # part 1
    # jdiff_count = {1:0, 2:0, 3:0}
    jdiff_count = Counter()
    for i in range(1,len(data)):
        jdiff = data[i] - data[i-1]
        jdiff_count[jdiff] += 1
    count1 = jdiff_count[1] * jdiff_count[3]
    
    # part 2
    ways = Counter((0, )) # init 0 count @ 1
    for j in data:
        ways[j] += sum(ways[i] for i in range(j - 3, j))
    count2 = ways[data[-1]]
        
    print("Step 1:", count1)
    print("Step 2:", count2)


