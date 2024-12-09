#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
input_file = "test01.txt"
# input_file = "test02.txt"


FREE_SPACE = "."


def checksum(disk_map):
    return sum(i * b for i, b in enumerate(disk_map) if b != FREE_SPACE)


def part1(disk_map):
    disk_map = disk_map[:] # create a copy
    for i, b in enumerate(disk_map[::-1]):
        if b == FREE_SPACE:
            continue
        next_free_space = disk_map.index(FREE_SPACE)
        if next_free_space >= (len(disk_map) - 1 - i):
            # free space after current file block
            break
        disk_map[next_free_space] = b
        disk_map[len(disk_map) - 1 - i] = FREE_SPACE
    return checksum(disk_map)


def part2(disk_map):

    return None


if __name__ == '__main__':
    disk_map = []
    with open(input_file, 'r') as f:
        map_str = f.readline().strip()
        file_id = 0
        for i, c in enumerate(map_str):
            if i % 2:
                content = FREE_SPACE
            else:
                content = file_id
                file_id += 1
            for j in range(int(c)):
                disk_map.append(content)
    print(part1(disk_map))
    print(part2(disk_map))
