# -*- coding: utf-8 -*-

input_file = [line.rstrip() for line in open('input.txt')]
sample_size = len(input_file)

def get_boxes():
    for s1 in input_file:
        for s2 in input_file:
            count = sum(1 for a, b in zip(s1, s2) if a != b)
            if count == 1:
                return s1, s2

s1, s2 = get_boxes()
for i in range(len(s1)):
    if s1[i] != s2[i]:
        break

print(s1[:i] + s1[i+1:]) #this won't include element [i]
