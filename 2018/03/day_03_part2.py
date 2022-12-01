# -*- coding: utf-8 -*-

import re

input_file = [line.rstrip() for line in open('input.txt')]
sample_size = len(input_file)
claims = []

claim_re = re.compile("#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)")

for s in input_file:
    claims.append([int(x) for x in claim_re.match(s).groups()])

x_max = max([(x + w) for id,x,y,w,h in claims])
y_max = max([(y + h) for id,x,y,w,h in claims])
claim_ids = {id for id,x,y,w,h in claims} # set

fabric = [[[0, []] for y in range(y_max)] for x in range(x_max)]

for c in claims:
    id,x,y,w,h = c
    for i in range(w):
        for j in range(h):
            fabric[x+i][y+j][0] += 1
            fabric[x+i][y+j][1].append(id)
            if fabric[x+i][y+j][0] > 1:
                for k in fabric[x+i][y+j][1]:
                    try:
                        claim_ids.remove(k)
                    except KeyError:
                        pass

print(claim_ids)



