#!/usr/bin/python

input_file = open("input", 'r')

planets = {}

for l in input_file.readlines():
    a,b = l.strip().split(")")
##    if a in planets:
##        planets[a].add(b)
##    else:
##        planets[a] = {b}
##    if b not in planets:
##        planets[b] = set()
    planets[b] = a # much easier with b)a as each planet orbits 1 single planet

def count_orbits(p):
    if p == "COM":
        return 0
    return count_orbits(planets[p]) + 1

nb_orbits = 0
for p in planets.keys():
   nb_orbits += count_orbits(p)
print("Part1:",nb_orbits)

def get_jumps(p):
    j = []
    while(True):
        j.append(p)
        if p == "COM":
            break
        p = planets[p]
    return j

# get jumps list to COM
j1 = get_jumps("YOU")
j2 = get_jumps("SAN")

# find first common planet in path
for p in j1:
    if p in j2:
        c = p
        break

print("Part2:", count_orbits("YOU") + count_orbits("SAN") - 2*count_orbits(c) - 2)
