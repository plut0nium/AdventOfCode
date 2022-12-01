#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

input_file = "input"
#input_file = "test1.txt"

lanternfish = defaultdict(int)
with open(input_file,'r') as f:
    for x in map(int, f.readline().strip().split(",")):
        lanternfish[x] += 1

def reproduce(school, timer):
    for i in range(timer):
        tmp = school[0]
        for a in range(8):
            school[a] = school[a+1]
        school[6] += tmp # reset parents
        school[8] = tmp # new fishes
    return school

print(sum(reproduce(lanternfish, 80).values()))
print(sum(reproduce(lanternfish, 256-80).values()))
        