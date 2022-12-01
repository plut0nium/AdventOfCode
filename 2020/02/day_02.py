#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
pw_re = re.compile("(\d+-\d+) ([a-zA-Z]{1}): (\w+)")

input_file = "input"

with open(input_file,'r') as f:
    pwds = [l.strip() for l in f.readlines()]

count1 = 0
count2 = 0

for p in pwds:
    por, poc, pw = pw_re.match(p).groups()
    pomin, pomax = list(map(int, por.split('-')))
    # step 1
    n = pw.count(poc)
    if n >= pomin and n <= pomax:
        count1 += 1
    # step 2
    pw = pw.strip()
    c = 0
    for i in [pomin, pomax]:
        if pw[i-1] == poc:
            c += 1
    if c == 1:
        count2 += 1
        
print("Step 1:", count1)
print("Step 2:", count2)


