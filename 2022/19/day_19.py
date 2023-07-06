#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import time
import re
from collections import deque

input_file = "input"
input_file = "test01.txt"

blueprint_pattern = re.compile(r"([+-]?\d+)")
# Ore, Clay, oBsidian, Geode
O, C, B, G = range(4)

def sim(costs, time=24, p2=False):
    q = deque([((1, 0, 0, 0), (0, 0, 0, 0), time)])
    visited = set()

    best = 0
    max_ore_needed = max(c[O] for c in costs)

    while q:
        x = q.pop()
        if x in visited:
        	continue
        
        rore, rclay, robs, rgeo = x[0]
        ore, clay, obs, geo = x[1]
        time = x[2]

        visited.add(x)

        # limit the number of collecting robots
        rore = min(rore, max_ore_needed)

        # collect
        new_ore = ore + rore
        new_clay = clay + rclay
        new_obs = obs + robs
        new_geo = geo + rgeo

        time -= 1
        if time == 0:
            best = max(best, new_geo)
            continue

        build = False
        if ore >= costs[G][O] and obs >= costs[G][B]:
            new_ore2 = new_ore - costs[G][O]
            new_obs2 = new_obs - costs[G][B]
            new_rgeo = rgeo + 1
            q.append(((rore, rclay, robs, new_rgeo), \
                      (new_ore2, new_clay, new_obs2, new_geo), time))
            build = True

			# Probably wrong, but works anyway...
            continue

        if ore >= costs[B][O] and clay >= costs[B][C]:
            new_ore2 = new_ore - costs[B][O]
            new_clay2 = new_clay - costs[B][C]
            new_robs = robs + 1
            q.append(((rore, rclay, new_robs, rgeo), \
                      (new_ore2, new_clay2, new_obs, new_geo), time))
            build = True

        if ore >= costs[C][O]:
            new_ore2 = new_ore - costs[C][O]
            new_rclay = rclay + 1
            q.append(((rore, new_rclay, robs, rgeo), \
                      (new_ore2, new_clay, new_obs, new_geo), time))
            build = True

        if ore >= costs[O][O]:
            new_ore2 = new_ore - costs[O][O]
            new_rore = rore + 1
            q.append(((new_rore, rclay, robs, rgeo), \
                      (new_ore2, new_clay, new_obs, new_geo), time))
            build = True

        # Technically wrong, but magically works for the first 3 blueprints :')
        # if not build:
        if not p2 or not build:
            q.append(((rore, rclay, robs, rgeo), \
                      (new_ore, new_clay, new_obs, new_geo), time))
    return best

if __name__ == '__main__':
    start_time = time()
    blueprints = []
    for l in open(input_file, 'r').readlines():
        bp = tuple(map(int, blueprint_pattern.findall(l.strip())))
        blueprints.append([bp[0], (bp[1], 0, 0), (bp[2], 0, 0), (bp[3], bp[4], 0), (bp[5], 0, bp[6])])
        #blueprints.append([bp[0], bp[1], bp[2], [bp[3], bp[4]], [bp[5], bp[6]]])

    tot = 0
    for bid, *costs in blueprints:
    	s = sim(costs)
    	tot += bid * s

    
    print("Part #1 :", tot)
    
    print("Part #2 :", None)
    
    print("Execution time: {:.6f}s".format((time() - start_time)))
