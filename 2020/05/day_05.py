#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import math
import re

input_file = "input"
#input_file = "test1.txt"

seat_dict = {"F":"0", "B":"1", "L":"0", "R":"1" } 

def get_seat_info(s):
    for key in seat_dict.keys():
        s = s.replace(key, seat_dict[key])
    return int(s, 2)

if __name__ == '__main__':
    
    with open(input_file,'r') as f:
        data = [l.strip() for l in f.readlines() if len(l.strip())>0]

    seat = [get_seat_info(s) for s in data]
    free = None

    # for i in range(2**10):
    #     if i not in seat and i-1 in seat and i+1 in seat:
    #         free = i
    seat.sort()
    for i in range(len(seat) - 1):
        if seat[i+1] != seat[i]+1:
            free = seat[i]+1
            break

    print("Step 1:", max(seat))
    print("Step 2:", free)


