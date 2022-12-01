# -*- coding: utf-8 -*-

import string

input_file = [line.rstrip() for line in open('input.txt')]
sample_size = len(input_file)
count2 = 0
count3 = 0

for s in input_file:
    found2 = False
    found3 = False
    for c in string.ascii_lowercase:
        j = s.count(c)
        if j == 2 and not found2:
            count2 += 1
            found2 = True
        elif j == 3 and not found3:
            count3 += 1
            found3 = True

print(count2, count3, count2 * count3)
