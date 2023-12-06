#!/usr/bin/python

img_x, img_y = 25,6
img_px = img_x * img_y

from PIL import Image

with open("input", 'r') as input_file:
    rawimg = [int(p) for p in input_file.readline().strip()]

img = [rawimg[i*img_px:(i+1)*img_px] for i in range(len(rawimg)//img_px)]

nb_zeros = len(img[0])
result = 0

for l in img:
    if l.count(0) < nb_zeros:
        nb_zeros = l.count(0)
        result = l.count(1) * l.count(2)

print("Part 1:",result)

img_render = [None for p in range(img_px)]

for p in range(img_px):
    for l in img:
        if l[p] != 2:
            img_render[p] = l[p]
            break

print("Part 2:")
for x,y in ((x,y) for y in range(img_y) for x in range(img_x)):
    if img_render[(y*img_x)+x] == 0:
        print(" ", end='')
    else:
        print("#", end='')
    if x == img_x - 1:
        print('')

img_file = Image.new("1", (img_x, img_y))
img_file.putdata(img_render)
img_file.save("day08.png")


    
