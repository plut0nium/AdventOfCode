# -*- coding: utf-8 -*-

frequencies = [0]
i = 0
j = 0
max_loop = 200

input_file = [int(line.rstrip()) for line in open('input.txt')]

while True:
    new_freq = frequencies[-1] + input_file[i]
    if new_freq in frequencies:
        print("Found : " + str(new_freq))
        break
    frequencies.append(new_freq)
    i += 1
    if i == len(input_file):
        i = 0
        j += 1
        print(j, end=' ')
    if j >= max_loop:
        break

print("Done.")
