#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
#input_file = "test01.txt"

def priority(i):
    p = ord(i.lower()) - ord('a') + 1
    if i.isupper():
        p += 26
    return p 

def part1(rucksacks):
    p = 0
    for r in rucksacks:
        c1 = set(r[:len(r)//2])
        c2 = set(r[len(r)//2:])
        common_item = c1.intersection(c2).pop()
        p += priority(common_item)
    return p

def part2(rucksacks):
    p = 0
    for i in range(len(rucksacks)//3):
        e1,e2,e3 = (e for e in map(set, rucksacks[i*3:i*3+3]))
        badge = e1.intersection(e2).intersection(e3).pop()
        p += priority(badge)
    return p

if __name__ == '__main__':
    with open(input_file) as f:
        rucksacks = f.read().strip().split('\n')
    
    print("Part #1 :", part1(rucksacks))
    print("Part #2 :", part2(rucksacks))
