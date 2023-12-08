#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"
# input_file = "test03.txt"

import math

START_NODE = "AAA"
END_NODE = "ZZZ"

def parse_map(map_lines):
    instructions = map_lines[0].strip()
    network = {}
    for n in map_lines[2:]:
        node, dir_str = n.strip().split(" = ")
        dir_left, dir_right = dir_str[1:-1].split(", ")
        network[node] = (dir_left, dir_right)
    return instructions, network

def browse(network, instructions, start, end, check_loop=False):
    step_count = 0
    current_node = start
    if isinstance(end, str):
        # part2 -> multiple end nodes
        end = [end]
    while current_node not in end \
          or (check_loop and step_count == 0):
        # force the first loop if check_loop as we may start from an end node
        direction = 0 if instructions[step_count % len(instructions)] == "L" else 1
        current_node = network[current_node][direction]
        step_count += 1
    return step_count, current_node

def part1(network, instructions):
    return browse(network, instructions, START_NODE, END_NODE)[0]

def part2(network, instructions):
    # assume each start node leads to a single end node
    # and that the paths are looped
    # see check below
    paths = []
    start_nodes = [n for n in network.keys() if n[-1] == "A"]
    end_nodes = [n for n in network.keys() if n[-1] == "Z"]
    for n in start_nodes:
        s, e = browse(network, instructions, n, end_nodes)
        # check loops
        # print(n, ">", e, "({})".format(s), end="")
        # for _ in range(3):
        #     s, e = browse(network, instructions, e, end_nodes, check_loop=True)
        #     print(">", e, "({})".format(s), end="")
        # print("")
        paths.append((n,e,s))
    return math.lcm(*(p[2] for p in paths))


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        instructions, network = parse_map(f.readlines())
    print("Part #1 :", part1(network, instructions))
    print("Part #2 :", part2(network, instructions))
