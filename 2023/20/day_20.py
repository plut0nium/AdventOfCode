#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.append("..")

from utils import timing

input_file = "input"
# input_file = "test01.txt"
# input_file = "test02.txt"

from enum import Enum
from collections import Counter
import math

class ModuleType(Enum):
    BROADCASTER = "b"
    FLIP_FLOP = "%"
    CONJUCTION = "&"
    NONE = "o"

class Pulse(Enum):
    LOW = 0
    HIGH = 1

# for part 2
RX = "rx"
button_spam = 0
cycles = Counter()

def parse_modules(input_lines):
    modules = {}
    inputs = {}
    for l in input_lines:
        mod_name, output_str = l.strip().split(" -> ")
        mod_type = ModuleType(mod_name[0])
        outputs = tuple(output_str.split(", "))
        if mod_type in (ModuleType.FLIP_FLOP, ModuleType.CONJUCTION):
            mod_name = mod_name[1:]
        for o in outputs:
            if o not in inputs:
                inputs[o] = []
            inputs[o].append(mod_name)
        modules[mod_name] = (mod_type, outputs, None)
    for n, m in modules.items():
        # update inputs for all conjunction modules
        mod_type, outputs, _ = m
        if mod_type == ModuleType.CONJUCTION:
            modules[n] = (mod_type, outputs, tuple(inputs[n]))
    return modules

def init_state(modules):
    # create & initialize state for modules:
    #  - dict of inputs for CONJUNCTIONs
    #  - internal LOW/HIGH for FLIP_FLOPs
    state = {}
    for n,m in modules.items():
        mod_type, _, inputs = m
        if mod_type == ModuleType.CONJUCTION:
            state[n] = {i:Pulse.LOW for i in inputs}
        elif mod_type == ModuleType.FLIP_FLOP:
            state[n] = Pulse.LOW
    return state

def pulse(modules, module_state, part2=None):
    pulse_counter = Counter()
    queue = []
    queue.append(("broadcaster", Pulse.LOW, None))
    global button_spam
    while len(queue):
        dest, pulse, source = queue.pop(0)
        pulse_counter[pulse] += 1
        # print(pulse, "to", dest, "from", source)
        if dest not in modules:
            # dummy output in test 02
            # print(f"Dummy module {dest} received {pulse} from {source}")
            continue
        if modules[dest][0] == ModuleType.BROADCASTER:
            for o in modules[dest][1]:
                queue.append((o, pulse, dest))
        elif modules[dest][0] == ModuleType.FLIP_FLOP:
            if pulse != Pulse.LOW:
                continue
            # toggle the value
            module_state[dest] = Pulse.HIGH if module_state[dest] == Pulse.LOW else Pulse.LOW  
            for o in modules[dest][1]:
                queue.append((o, module_state[dest], dest))
        elif modules[dest][0] == ModuleType.CONJUCTION:
            if part2 is not None:
                # part 2
                if dest == part2 and pulse == Pulse.HIGH and source not in cycles:
                    cycles[source] = button_spam
                if all(s in cycles for s in modules[dest][2]):
                    # we have trigger times for all inputs
                    return None, None
            module_state[dest][source] = pulse
            if all(i == Pulse.HIGH for i in module_state[dest].values()):
                output = Pulse.LOW
            else:
                output = Pulse.HIGH
            for o in modules[dest][1]:
                queue.append((o, output, dest))
        else:
            pass
    return module_state, pulse_counter

@timing
def part1(modules, button_push=4):
    module_state = init_state(modules)
    pulse_counter = Counter()
    for _ in range(button_push):
        module_state, count = pulse(modules, module_state)
        pulse_counter.update(count)
    return pulse_counter[Pulse.LOW] * pulse_counter[Pulse.HIGH]

@timing
def part2(modules):
    module_state = init_state(modules)
    global button_spam
    # part 2 -> find the input to RX
    rx_input = [k for k,v in modules.items() if RX in v[1]]
    assert(len(rx_input) == 1) # we expect only 1 input to RX
    rx_input = rx_input.pop(0)
    assert(modules[rx_input][0] == ModuleType.CONJUCTION)
    while module_state is not None:
        button_spam += 1
        module_state, _ = pulse(modules, module_state, rx_input)
    return math.lcm(*cycles.values())


if __name__ == '__main__':
    with open(input_file, 'r') as f:
        modules = parse_modules(f.readlines())
    print("Part #1 :", part1(modules, 1000))
    print("Part #2 :", part2(modules))
