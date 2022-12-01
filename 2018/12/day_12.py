#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test1.txt"

direction = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}
rotation = ['N','E','S','W']

def move_ship(pos, orn, ins):
    if ins[0] in direction:
        pos = (pos[0]+direction[ins[0]][0]*ins[1],pos[1]+direction[ins[0]][1]*ins[1])
    elif ins[0] == 'F':
        pos = (pos[0]+direction[orn][0]*ins[1],pos[1]+direction[orn][1]*ins[1])
    elif ins[0] in ('L','R'):
        d = -1 if ins[0] == 'L' else 1
        orn = rotation[(rotation.index(orn)+int(ins[1]/90*d))%len(rotation)]
    else:
        # ERROR
        pass
    return pos, orn

def move_wp(pos, pos_wp, ins):
    if ins[0] in direction:
        pos_wp = (pos_wp[0]+direction[ins[0]][0]*ins[1],pos_wp[1]+direction[ins[0]][1]*ins[1])
    elif ins[0] == 'F':
        pos = (pos[0]+pos_wp[0]*ins[1],pos[1]+pos_wp[1]*ins[1])
    elif ins[0] in ('L','R'):
        d = (-1,1) if ins[0] == 'L' else (1,-1)
        a = int(ins[1] / 90)
        for i in range(a):
            pos_wp = (pos_wp[1]*d[0],pos_wp[0]*d[1])
    else:
        # ERROR
        pass
    return pos, pos_wp


if __name__ == '__main__':
    count1, count2 = 0, 0

    with open(input_file,'r') as f:
        data = [(l.strip()[0], int(l.strip()[1:])) for l in f.readlines() if l.strip()]

    # part 1
    pos = (0,0)
    orn = 'E'

    # part 2
    pos2 = (0,0)
    pos_wp = (10,1)

    for i in data:
        pos, orn = move_ship(pos, orn, i)
        # print(pos, orn)
        pos2, pos_wp = move_wp(pos2, pos_wp, i)
        # print(pos2, pos_wp)

    count1 = abs(pos[0])+abs(pos[1])
    count2 = abs(pos2[0])+abs(pos2[1])

    print("Step 1:", count1)
    print("Step 2:", count2)


