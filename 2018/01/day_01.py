# -*- coding: utf-8 -*-

frequency = 0

input_file = open('input.txt')
for i in input_file:
    frequency += int(i)

print(frequency)

