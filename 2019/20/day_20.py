#!/usr/bin/env python
# -*- coding: utf-8 -*-

from grid import Grid

input_file = "input20_test1.txt"

if __name__ == '__main__':
    maze = Grid('.')
    x,y = 0,0
    portals = {}
    with open(input_file, 'r') as f:
        for l in f.readlines():
            for m in l.strip('\n'):
                maze.set(x,y,m)
                x += 1
            y += 1
            x = 0
    # set origin at @
    maze.set_origin(2, 2)
    outer_width = maze.width() - 4
    outer_height = maze.height() - 4
    # find maze thickness
    y = outer_height // 2
    while True:
        if not any(m.isupper() for m in [maze.get(x,y) for x in range(outer_width)]):
            for xi in range(outer_width // 2):
                if maze.get(xi,y) == " ":
                    thickness = xi
                    break
            break
        else:
            y += 1 
    # find portals
    # thickness,outer_width-thickness-1
    for x in (-2,outer_width):
        for y in range(outer_height):
            m = maze.get(x,y)
            if m.isupper():
                port_name = m + maze.get(x+1,y) + 'o'
                print(port_name)
    
    
    
    
    print(maze.render())
    print("Part 1:", None)
