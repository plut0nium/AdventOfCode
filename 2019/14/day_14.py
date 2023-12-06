#!/usr/bin/python
# -*- coding: utf-8 -*-

import math
from collections import defaultdict

input_file = "input14.txt"
#input_file = "input_test04.txt"

reactions = {}
inventory = {}

with open(input_file,'r') as f:
    for l in f.readlines():
        reaction = l.split("=>")
        reactants = reaction[0].strip().split(",")
        nu_p, prod = reaction[1].strip().split(" ")
        nu_p = int(nu_p)
        reactions[prod] = [nu_p, []]
        for r in reactants:
            nu_r, reac = r.strip().split(" ")
            nu_r = int(nu_r)
            reactions[prod][1].append((reac, nu_r))
            if reac not in reactions:
                # make sure we have all chemicals in reactions
                # ORE should be the only left to None
                reactions[reac] = None


needed = defaultdict(int)
producing = defaultdict(int)

def produce(chemical):
    count = math.ceil(max(0, needed[chemical] - producing[chemical]) / reactions[chemical][0])
    producing[chemical] += count * reactions[chemical][0]
    for r,n in reactions[chemical][1]:
        needed[r] += count * n
    for r,n in reactions[chemical][1]:
        if r != "ORE":
            produce(r)

needed["FUEL"] = 1
produce("FUEL")
print("Part 1:",needed["ORE"])

ore_reserve = 1000000000000
fuel_to_produce = 0
fuel_jump = 1
narrowing = False

while True:
    needed.clear()
    producing.clear()
    needed["FUEL"] = fuel_to_produce
    produce("FUEL")
    if needed["ORE"] > ore_reserve:
        narrowing = True
        fuel_jump = max(1, fuel_jump // 2)
        fuel_to_produce -= fuel_jump
    elif not narrowing:
        fuel_jump *= 2
        fuel_to_produce += fuel_jump
    else:
        if fuel_jump == 1:
            break
        fuel_to_produce += fuel_jump

print("Part 2:", fuel_to_produce)

