#!/usr/bin python

import math
from copy import deepcopy

from datetime import datetime
start_time = datetime.now()

input_file = "input"
#input_file = "input_test2.txt"

def locate_asteroids(input_file):
    with open(input_file, 'r') as f:
        a = f.readlines()
    x, y = 0, 0
    asteroids = []
    for l in a:
        for p in l.strip():
            if p == "#":
                asteroids.append((x,y))
            x += 1
        x = 0
        y += 1
    return asteroids

def get_angle_distance(a, b):
    ax, ay = a
    bx, by = b
    dx = bx - ax
    dy = ay - by # y-axis is inverted
    if ax == bx and ay == by:
        return 0.0, 0.0
    # angle is measured clockwise from the UP direction
    angle = math.pi / 2.0 - math.atan2(dy,dx)
    if angle < 0.0:
        angle = math.pi * 2.0 + angle
    distance = math.sqrt(dy ** 2.0 + dx ** 2.0)
    return angle, distance

if __name__ == '__main__':
    a_list = locate_asteroids(input_file)

    # Part 1
    vis_count = []
    for a in a_list:
        visible = {}
        for angle,dist in [get_angle_distance(a,b) for b in a_list]:
            if dist == 0.0:
                continue
            visible[angle] = dist
        vis_count.append(len(visible))

    print("Part 1:", max(vis_count))

    # Part 2
    station = a_list[vis_count.index(max(vis_count))]
    a_list_rel = [get_angle_distance(station,b) for b in a_list]
    to_vaporize = deepcopy(a_list_rel)
    to_vaporize.remove((0.0,0.0)) # we don't want to vaporize ourselves
    angles = sorted(set([t[0] for t in to_vaporize]))
    vaporized = []
    while(True):
        # loop through all angles
        for a in angles:
            # find the closest asteroid at this angle
            closest = 0.0
            for t in to_vaporize:
                if t[0] != a:
                    continue
                if closest == 0.0 or t[1] < closest:
                    closest = t[1]
            if closest == 0.0:
                # no asteroid found at this angle
                angles.remove(a)
                continue
            # vaporize it !
            to_vaporize.remove((a, closest))
            vaporized.append(a_list[a_list_rel.index((a, closest))])
            #print(vaporized, ">>>", a, closest)
        if len(angles) == 0:
            break
    
    w_coords = vaporized[199]
    print("Part 2:", w_coords[0]*100+w_coords[1])
                
#print(datetime.now() - start_time)
