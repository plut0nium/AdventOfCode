#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test1.txt"

gamma = ""

with open(input_file,'r') as f:
    diagnostic = [r.strip() for r in f.readlines()]

rows = len(diagnostic)
cols = len(diagnostic[0])
dmask = int("1"*cols,base=2)

for i in range(cols):
    column = "".join(c[i] for c in diagnostic)
    ones = column.count("1")
    if ones >= (rows - ones):
        gamma += "1"
    else:
        gamma += "0"

gamma_rate = int(gamma, base=2)
epsilon_rate = ~gamma_rate & dmask
print(gamma_rate * epsilon_rate)

def filter(d, inverse=False):
    d2 = set(d)
    for i in range(len(d[0])):
        column = "".join(c[i] for c in d2)
        ones = column.count("1")
        if (not inverse and ones >= (len(d2) - ones)) \
            or (inverse and ones < (len(d2) - ones)):
            bit = "0"
        else:
            bit = "1"
        d2 = d2 - set(c for c in d2 if c[i] == bit)
        if len(d2) == 1:
            break
    return d2

oxygen_generator_rating = int(max(filter(diagnostic)), base=2)
co2_scrubber_rating = int(max(filter(diagnostic, True)), base=2)

print(oxygen_generator_rating * co2_scrubber_rating)

