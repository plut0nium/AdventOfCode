# -*- coding: utf-8 -*-

import re
from datetime import datetime
import numpy as np

input_file = [line.rstrip() for line in open('input.txt')]
input_file.sort() # sort alphabeticaly is enough
sample_size = len(input_file)
guards = {}
current_guard = None
sleeping_from = None

log_re = re.compile("\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (Guard #(\d+) begins shift|falls asleep|wakes up)")

for l in input_file:
    log_entry = log_re.match(l).groups()
    timestamp = datetime.fromisoformat(log_entry[0])
    if log_entry[2] is not None and log_entry[2].isdigit():
        current_guard = int(log_entry[2])
        if current_guard not in guards:
            guards[current_guard] = np.zeros(60)
    elif "falls asleep" in log_entry[1]:
        sleeping_from = timestamp
    elif "wakes up" in log_entry[1]:
        for m in range(sleeping_from.minute, timestamp.minute):
            guards[current_guard][m] += 1
        sleeping_from = None
    else:
        pass # we shouldn't be here

#part 1
biggest_sleeper = max(guards.items(), key=lambda k: sum(k[1]))
print(biggest_sleeper[0] * biggest_sleeper[1].argmax())

#part 2
frequent_sleeper = max(guards.items(), key=lambda k: max(k[1]))
print(frequent_sleeper[0] * frequent_sleeper[1].argmax())



