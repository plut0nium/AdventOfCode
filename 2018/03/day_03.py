# -*- coding: utf-8 -*-

import re
import numpy as np

input_file = [line.rstrip() for line in open('input.txt')]
sample_size = len(input_file)
claims = []

claim_re = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

for s in input_file:
    claims.append([int(x) for x in claim_re.match(s).groups()])

x_max = max([(x + w) for id,x,y,w,h in claims])
y_max = max([(y + h) for id,x,y,w,h in claims])

fabric = np.zeros((x_max, y_max), dtype=int)

for c in claims:
    id,x,y,w,h = c
    for i in range(w):
        for j in range(h):
            fabric[x+i][y+j] += 1

unique, counts = np.unique(fabric, return_counts=True)
count_dict = dict(zip(unique, counts))

result = (x_max * y_max) - (count_dict[0] + count_dict[1])

print(result)




