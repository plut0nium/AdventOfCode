#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
from itertools import combinations
from functools import reduce
from math import gcd
from copy import deepcopy

input_file = "input"
#input_file = "input_test.txt"
#input_file = "input_test2.txt"
steps = 1000

moon_pos = []
moon_vel = []
nb_moon = 0

with open(input_file,'r') as f:
    for l in f.readlines():
        x,y,z = map(int, re.findall(r'[-+]?\d+', l))
        moon_pos.append([x,y,z])
        
nb_moon = len(moon_pos)
moon_vel = [[0,0,0] for m in range(nb_moon)]

moon_pos_initial = deepcopy(moon_pos)
moon_vel_initial = deepcopy(moon_vel)

def apply_gravity():
    for m1,m2 in combinations(range(nb_moon),2):
        for axis in range(3):
            if moon_pos[m1][axis] > moon_pos[m2][axis]:
                moon_vel[m1][axis] -= 1
                moon_vel[m2][axis] += 1
            elif moon_pos[m1][axis] < moon_pos[m2][axis]:
                moon_vel[m1][axis] += 1
                moon_vel[m2][axis] -= 1

def apply_velocity():
    for m in range(nb_moon):
        for axis in range(3):
            moon_pos[m][axis] += moon_vel[m][axis]

def total_energy():
    e = 0
    for m in range(nb_moon):
        e_pot = sum(map(abs,moon_pos[m]))
        e_kin = sum(map(abs,moon_vel[m]))
        e += e_pot * e_kin
    return e
    
for s in range(steps):
    apply_gravity()
    apply_velocity()

print("Part 1:", total_energy())

# reset
moon_pos = moon_pos_initial
moon_vel = moon_vel_initial

def get_universe_state():
    return [([moon_pos[m][a] for m in range(nb_moon)], \
             [moon_vel[m][a] for m in range(nb_moon)]) for a in range(3)]

# the first state to repeat will always be the initial state
initial_state = get_universe_state()

period = [0,0,0]

steps = 0
while(True):
    steps += 1
    apply_gravity()
    apply_velocity()
    u_state = get_universe_state()
    for axis in range(3):
        if initial_state[axis] == u_state[axis] and period[axis] == 0:
            period[axis] = steps
    if not any(i==0 for i in period):
        break

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcm3(a):
    """Return lcm of args."""   
    return reduce(lcm, a)

print("Part 2:", lcm3(period))


    