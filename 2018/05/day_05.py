# -*- coding: utf-8 -*-

import string

input_line = open('input.txt').readline().strip()

def are_reacting(a, b):
    return (a != b) and (a.lower() == b.lower())

def react(line):
    buf = []
    for c in line:
        if buf and are_reacting(c, buf[-1]):
            buf.pop()
        else:
            buf.append(c)
    return len(buf)

#agents = string.ascii_lowercase
agents = set([c.lower() for c in input_line])

# part 1
print(react(input_line))

# part 2
print(min([react(input_line.replace(a, '').replace(a.upper(), '')) for a in agents]))
