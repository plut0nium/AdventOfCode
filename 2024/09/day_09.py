#!/usr/bin/env python
# -*- coding: utf-8 -*-

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"


FREE_SPACE = "."


def checksum(disk_map):
    # checksum of an unpacked disk
    return sum(i * b for i, b in enumerate(disk_map) if b != FREE_SPACE)


def unpack(disk_map):
    unpacked = []
    for b in disk_map:
        unpacked.extend([b[1]] * b[0])
    return unpacked


def part1(disk_map):
    disk_map = unpack(disk_map)
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

    def find_next_free_space(disk_map, min_size=0):
        for i, b in enumerate(disk_map):
            if b[1] == FREE_SPACE \
               and b[0] >= min_size:
                return i
        return None

    for b in [b for b in disk_map[::-1] if b[1] != FREE_SPACE]:
        file_index = disk_map.index(b)
        next_free_space = find_next_free_space(disk_map, b[0])
        if next_free_space is None \
           or next_free_space >= file_index:
            # no available space
            continue
        if disk_map[next_free_space][0] == b[0]:
            #replace
            disk_map[next_free_space] = b
            disk_map[file_index] = (b[0], FREE_SPACE) # could merge free spaces
        else:
            #split
            disk_map.insert(next_free_space, b)
            disk_map[next_free_space+1] = (disk_map[next_free_space+1][0] - b[0], FREE_SPACE)
            disk_map[file_index+1] = (b[0], FREE_SPACE)
    return checksum(unpack(disk_map))


if __name__ == '__main__':
    disk_map = []
    with open(input_file, 'r') as f:
        map_str = f.readline().strip()
        file_id = 0
        for i, c in enumerate(map_str):
            if not int(c):
                # empty file/free space
                continue
            if i % 2:
                content = FREE_SPACE
            else:
                content = file_id
                file_id += 1
            disk_map.append((int(c), content))
    print(part1(disk_map))
    print(part2(disk_map))
