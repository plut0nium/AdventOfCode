#!/usr/bin/python


def make_coords(wire):
    coords = []
    origin = (0,0)
    coords.append(origin)
    for s in wire:
        x1,y1 = coords[-1]
        direction,distance = s[0],int(s[1:])
        if direction == "U":
            c = (x1, y1 + distance)
        elif direction == "D":
            c = (x1, y1 - distance)
        elif direction == "R":
            c = (x1 + distance, y1)
        elif direction == "L":
            c = (x1 - distance, y1)
        coords.append(c)
    return coords

def intersect(w1,w2):
    #print("testing",w1,w2)
    if w1[0][0] == w1[1][0] and w2[0][0] == w2[1][0]:
        #print("Both vertical")
        return False # both segments are vertical
    if w1[0][1] == w1[1][1] and w2[0][1] == w2[1][1]:
        #print("Both horizontal")
        return False # both segments are horizontal
    if w1[0][0] == w1[1][0]:
        # segment1 is vertical:
        pass
    else:
        # segment1 is horizontal:
        w1,w2 = w2,w1
    if (w1[0][0] <= min(w2[0][0],w2[1][0])) or (w1[0][0] >= max(w2[0][0],w2[1][0])):
        return False
    if (w2[0][1] <= min(w1[0][1],w1[1][1])) or (w2[0][1] >= max(w1[0][1],w1[1][1])):
        return False
    #print("Intersect @", w1[0][0],",",w2[0][1])
    return (w1[0][0],w2[0][1])


if __name__ == "__main__":
    input_file = open("input", 'r')
    wires = [l.split(",") for l in input_file.readlines()]

    closest_intersect = 0
    shortest_intersect = 0

    wires_coords = [make_coords(w) for w in wires]

    for i in range(1, len(wires_coords[0])):
        for j in range(1, len(wires_coords[1])):
            x = intersect((wires_coords[0][i-1],wires_coords[0][i]),
                          (wires_coords[1][j-1],wires_coords[1][j]))
            if x is not False:
                distance = abs(x[0]) + abs(x[1])
                closest_intersect = min(distance, closest_intersect) if closest_intersect != 0 else distance
                # part 2
                length1, length2 = 0,0
                # wire 1
                for k in range(1,i):
                    length1 += abs(wires_coords[0][k-1][0] - wires_coords[0][k][0]) + \
                               abs(wires_coords[0][k-1][1] - wires_coords[0][k][1])
                # last segment only to intersection
                length1 += abs(wires_coords[0][i-1][0] - x[0]) + \
                           abs(wires_coords[0][i-1][1] - x[1])
                # wire 2
                for l in range(1,j):
                    length2 += abs(wires_coords[1][l-1][0] - wires_coords[1][l][0]) + \
                               abs(wires_coords[1][l-1][1] - wires_coords[1][l][1])
                # last segment only to intersection
                length2 += abs(wires_coords[1][j-1][0] - x[0]) + \
                           abs(wires_coords[1][j-1][1] - x[1])
                length = length1 + length2
                shortest_intersect = min(length, shortest_intersect) if shortest_intersect != 0 else length
                
    print("Part1:", closest_intersect)
    print("Part2:", shortest_intersect)
                
        
