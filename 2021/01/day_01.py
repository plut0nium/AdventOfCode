#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"

if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        depth_scan = list(map(int, f.readlines()))
    
    for i in range(1, len(depth_scan)):
        if depth_scan[i] > depth_scan[i-1]:
            count1 += 1
    
    print(count1)
    
    window_size = 3
    
#    w = [sum(depth_scan[i-2:i+1]) for i in range(window_size-1,len(depth_scan))]
    
#    for i in range(1, len(w)):
#        if w[i] > w[i-1]:
#            count2 += 1
    
    # if A+B+C > B+C+D, then A > D...
    for i in range(window_size,len(depth_scan)):
        if depth_scan[i] > depth_scan[i-window_size]:
            count2 += 1
    
    print(count2)
