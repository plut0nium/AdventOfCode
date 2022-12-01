#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test1.txt"

crabs = defaultdict(int)
with open(input_file,'r') as f:
    for c in map(int, f.readline().strip().split(",")):
        crabs[c] += 1

fuel1 = []
fuel2 = []
for p in range(min(crabs.keys()), max(crabs.keys())+1):
    f1,f2 = 0, 0
    for c in crabs.keys():
        dist = abs(c - p)
        f1 += dist * crabs[c]
        f2 += int(dist * (dist + 1) / 2) * crabs[c] # n*(n+1)/2 = sum(1..n)
    fuel1.append(f1)
    fuel2.append(f2)

print(min(fuel1))
print(min(fuel2))
    