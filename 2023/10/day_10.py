#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"
# input_file = "test04.txt"
# input_file = "test05.txt"
# input_file = "test06.txt"

PIPES = { "|": ("N", "S"),
          "-": ("W", "E"),
          "L": ("N", "E"),
          "J": ("N", "W"),
          "7": ("S", "W"),
          "F": ("S", "E")  
        }
GROUND = "."
START = "S"
DIRECTIONS = { "NW": (-1, -1), "N" : ( 0, -1), "NE": ( 1, -1),
               "W" : (-1,  0),                 "E" : ( 1,  0),              
               "SW": (-1,  1), "S" : ( 0,  1), "SE": ( 1,  1)
             }

import re

loop_edge = re.compile(r'\||L-*7|F-*J')

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

def _get_connection(x, y, sym):
    # return the connected tiles
    # given the shape of the pipe
    assert(sym in PIPES)
    connected = []
    for s in PIPES[sym]:
        d = DIRECTIONS[s]
        connected.append((x+d[0], y+d[1]))
    return connected

def _get_adjacent(x, y, sym=None):
    # return adjacent tiles
    # that are NOT connected
    # assert(sym in PIPES)
    adjacent = []
    for s in set(("N","E","S","W")).difference(PIPES[sym] if sym in PIPES else []):
        d = DIRECTIONS[s]
        adjacent.append((x+d[0], y+d[1]))
    return adjacent

def _grid_size(grid):
    x, y = map(set, zip(*grid.keys()))
    return min(x), max(x), min(y), max(y)

def navigate_pipes(pipes, pos):
    current_pos = pos
    path = [pos]
    while pipes[current_pos] != START:
        x, y = current_pos
        for c in _get_connection(x, y, pipes[current_pos]):
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
        if start_pos in _get_connection(x, y, pipes[(x,y)]):
            connected_to_start.append((x,y))
    assert(len(connected_to_start) == 2)
    # start in 1 direction
    c = connected_to_start[0]
    path = navigate_pipes(pipes, c)
    return path

def part2(pipes, loop):
    regions = []
    x_min, x_max, y_min, y_max = _grid_size(pipes)

    def _is_free(tile):
        if tile[0] < x_min or tile[0] > x_max \
            or tile[1] < y_min or tile[1] > y_max:
            # out of grid
            return False
        elif tile in loop:
            # in the loop
            return False
        elif any((tile in r for r in regions)):
            # tile is known
            return False
        return True

    def _new_region(tile):
        # build a new region starting from tile
        r = [tile]
        def _expand(tile):
            # print(">>>", tile)
            for t in _get_adjacent(tile[0], tile[1]):
                if _is_free(t) and t not in r:
                    r.append(t)
                    _expand(t)
        _expand(tile)
        return r          
        
    for p in loop:
        x, y = p
        a = _get_adjacent(x, y, pipes[p])
        for t in a:
            if _is_free(t):            
                # build a new region
                regions.append(_new_region(t))
    # print(len(regions))
    # remove all regions touching the edges
    regions_filtered = []
    for r in regions:
        if any(((t[0] in (x_min, x_max)) or (t[1] in (y_min, y_max)) for t in r)):
            continue
        regions_filtered.append(r)
    # print(len(regions_filtered))
    # check if region is enclosed
    enclosed = 0
    for r in regions_filtered:
        x, y = r[0]
        to_edge = "".join((pipes[(d,y)] for d in range(x) if (d,y) in loop))
        # print(x, y, to_edge)
        if len(loop_edge.findall(to_edge)) % 2:
            enclosed += len(r)
    return enclosed


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        pipes, start_pos = parse_pipes(f.readlines())
    loop = part1(pipes, start_pos)
    print("Part #1 :", len(loop) // 2)
    print("Part #2 :", part2(pipes, loop))
