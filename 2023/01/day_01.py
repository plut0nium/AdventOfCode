#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

DIGITS = "1234567890"
DIGITS_AS_WORDS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def calibration(s):
    v = [c for c in s if c in DIGITS]
    if len(v) == 0:
        return 0
    return int(v[0] + v[-1])

def calibration2(s):
    s2 = []
    for i, c in enumerate(s):
        if c in DIGITS:
            s2.append(int(c))
            continue
        for word, digit in DIGITS_AS_WORDS.items():
            if s[i:].startswith(word):
                s2.append(digit)
                break
    return s2[0] * 10 + s2[-1]
                
        
if __name__ == '__main__':
    p1 = 0
    p2 = 0
    for l in open(input_file, 'r').readlines():
        p1 += calibration(l.strip())
        p2 += calibration2(l.strip())
    print("Part #1 :", p1)
    print("Part #2 :", p2)
