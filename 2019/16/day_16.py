#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
start_time = datetime.now()

pattern = [0, 1, 0, -1]

def FFT(signal, pattern, phases):
    input_signal = [x for x in signal]
    for p in range(phases):
        output = []
        for s in range(len(signal)):
            output.append(0)
            #construct pattern
            pat = [a for a in pattern for b in range(s+1)]
            for i in range(len(input_signal)):
                output[s] += input_signal[i] * pat[(i + 1) % len(pat)]
            output[s] = abs(output[s]) % 10
        input_signal = [x for x in output]
    return output

def FFT_optimized(signal, phases):
    input_signal = [x for x in signal]
    for p in range(phases):
        output = [0] * len(signal)
        output[-1] = input_signal[-1]
        for s in range(len(signal)-2, -1, -1):
            output[s] = input_signal[s] + output[s+1]
            output[s] %= 10
        input_signal = [x for x in output]
    return output

if __name__ == '__main__':
    with open("input16.txt", 'r') as f:
        signal = f.read().strip()
        signal = [int(x) for x in signal]
        
    # TEST1
#   print(FFT([1,2,3,4,5,6,7,8],pattern,4))
    # TEST 2 - 4 
#    tests = ["80871224585914546619083218645595",
#             "19617804207202209144916044189917",
#             "69317163492948606335995924319873"]
#    for t in tests:
#        print(FFT([int(x) for x in t],pattern,100)[:8])

    part1 = int("".join(map(str, FFT(signal, pattern, 100)[:8])))
    print("Part 1:", part1)

#    print(datetime.now() - start_time)

#    tests = ["03036732577212944063491565474664",
#             "02935109699940807407585447034323",
#             "03081770884921959731165446850517"]
#    for t in tests:
#        offset = int("".join(map(str, t[:7])))
#        signal = [int(x) for x in t]*10000
#        print(FFT_optimized(signal[offset:],100)[:8])

    offset = int("".join(map(str, signal[:7])))    
    signal = signal * 10000
    assert(offset > len(signal)/2) # if True we can use the optimized FFT
    part2 = int("".join(map(str, FFT_optimized(signal[offset:],100)[:8])))
    print("Part 2:", part2)

#    print(datetime.now() - start_time)