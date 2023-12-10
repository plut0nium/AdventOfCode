#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"


PIPES = { "|": ("N", "S"),
          "-": ("W", "E"),
          "L": ("N", "E"),
          "J": ("N", "W"),
          "7": ("S", "W"),
          "F": ("S", "E")  
        }
DIRECTIONS = { "N": ( 0, -1),
               "S": ( 0,  1),
               "E": ( 1,  0),
               "W": (-1,  0)  
             }
GROUND = "."
START = "S"

def parse_pipes(pipes_list):
    pipes = {}
    start_pos = None
    for y, l in enumerate(pipes_list):
        for x, p in enumerate(l.strip()):
            if p == GROUND:
                continue
            elif p in PIPES:
                pipes[(x,y)] = p
            elif p == START:
                start_pos = (x,y)
                pipes[(x,y)] = p
    return pipes, start_pos

def _get_connection(sym, x, y):
    # return the connected coordinates
    # given the shape of the pipe
    assert(sym in PIPES)
    connected = []
    for s in PIPES[sym]:
        d = DIRECTIONS[s]
        connected.append((x+d[0], y+d[1]))
    return connected

def navigate_pipes(pipes, pos):
    current_pos = pos
    path = [pos]
    while pipes[current_pos] != START:
        x, y = current_pos
        for c in _get_connection(pipes[current_pos], x, y):
            if c in path:
                continue
            if pipes[c] == START and len(path) < 2:
                # trick to avoid loop on initial position
                continue
            current_pos = c
            path.append(c)
    return path

def part1(pipes, start_pos):
    connected_to_start = []
    # find pipes connecting to S
    for _, d in DIRECTIONS.items():
        x, y = start_pos[0] + d[0], start_pos[1] + d[1]
        if (x,y) not in pipes:
            continue
        if start_pos in _get_connection(pipes[(x,y)], x, y):
            connected_to_start.append((x,y))
    assert(len(connected_to_start) == 2)
    # start in 1 direction
    c = connected_to_start[0]
    path = navigate_pipes(pipes, c)
    return path

def part2(pipes):
    return None


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        pipes, start_pos = parse_pipes(f.readlines())
    loop = part1(pipes, start_pos)
    print("Part #1 :", len(loop) // 2)
    print("Part #2 :", part2(pipes))
