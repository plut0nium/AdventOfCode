#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"

target = 2020

with open(input_file,'r') as f:
    data = [int(l) for l in f.readlines()]

for d in data:
    r = target - d
    if r in data:
        print("Step 1:", d * r)
        break


for i in range(len(data)):
    d = data[i]
    t2 = target - d
    for d2 in data[i+1:]:
        r2 = t2 - d2
        if r2 in data[i+1:]:
            print("Step 2:", d * d2 * r2)
            break

