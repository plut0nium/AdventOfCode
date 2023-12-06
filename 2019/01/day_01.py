#!/usr/bin/python

import math

i = open("input", 'r')
result1 = 0
result2 = 0

def calc_fuel(x):
    if (x >= 9):
        y = math.floor(x / 3) - 2
        return (y + calc_fuel(y))
    else:
        return 0

for l in i.readlines():
    m = int(l.strip())
    result1 += math.floor(m / 3) - 2
    result2 += calc_fuel(m)

print(result1)
print(result2)



