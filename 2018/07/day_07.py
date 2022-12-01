# -*- coding: utf-8 -*-

import re
import itertools

dep_re = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

dependencies = [tuple(dep_re.match(line).groups()) for line in open('input.txt')]

tasks = {t for t in itertools.chain(*dependencies)}
task_ready = list(tasks.difference([d[1] for d in dependencies]))

# PART 1
task_finished = []

while len(task_ready) > 0:
    task_ready.sort()
    task_finished.append(task_ready.pop(0))
    to_remove = []
    for d in dependencies:
        if d[0] == task_finished[-1]:
            to_remove.append(d) # we should not modify the list while iterating
    for d in to_remove:
        dependencies.remove(d)
    task_ready.extend(list(tasks.difference(task_finished)
                                .difference(task_ready)
                                .difference([d[1] for d in dependencies])))
    #print(task_ready)

print(''.join(task_finished))

# PART 2

dependencies = [tuple(dep_re.match(line).groups()) for line in open('input.txt')]

tasks = {t for t in itertools.chain(*dependencies)}
task_ready = list(tasks.difference([d[1] for d in dependencies]))

nb_workers = 5
worker = [[None,0] for i in range(nb_workers)]
task_finished = []
time = 0

while len(task_finished) < len(tasks):
    task_ready.sort()
    time += 1
    for i in range(nb_workers):
        worker[i][1] -= 1
        if worker[i][1] <= 0: # worker is available
            if worker[i][0] is not None:
                task_finished.append(worker[i][0])
                worker[i][0] = None
                to_remove = []
                for d in dependencies:
                    if d[0] in task_finished:
                        to_remove.append(d) # we should not modify the list while iterating
                for d in to_remove:
                    dependencies.remove(d)
                task_ready.extend(list(tasks.difference(task_finished)
                                            .difference(task_ready)
                                            .difference([w[0] for w in worker])
                                            .difference([d[1] for d in dependencies])))
            if len(task_ready) > 0:
                worker[i][0] = task_ready.pop(0)
                worker[i][1] = ord(worker[i][0]) - 4
print(time-1)