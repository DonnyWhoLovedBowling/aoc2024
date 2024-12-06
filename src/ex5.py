from math import floor
from copy import deepcopy


def is_ordered(_update):
    _is_ordered = True
    for _i in range(len(_update)):
        _page_before = _update[_i]
        for _j in range(_i+1, len(_update)):
            _page_after = _update[_j]
            if _page_after in rules:
                pages_before = set(_update[0:_j])
                if not pages_before.isdisjoint(rules[_page_after]):
                    _is_ordered = False
            if not _is_ordered:
                break
        if not _is_ordered:
            break
    return _is_ordered


in_file = open("../data/ex5.txt")
lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
rules = dict()
updates = []
updates_2 = []
total_1 = 0
total_2 = 0

for line in lines:
    if '|' in line:
        splt = line.split('|')
        if splt[0] in rules:
            rules[splt[0]].add(splt[1])
        else:
            rules[splt[0]] = {splt[1]}
    elif line == '':
        continue
    else:
        updates.append(line.split(','))

for update in updates:
    if is_ordered(update):
        total_1 += int(update[floor((len(update)/2))])
    else:
        updates_2.append(update)

print(total_1)

for update in updates_2:
    new_update = deepcopy(update)
    while True:
        iter += 1
        for i in range(len(new_update)-1):
            page_before = new_update[i]
            page_after = new_update[i+1]
            if page_after in rules:
                if page_before in rules[page_after]:
                    new_update[i], new_update[i+1] = new_update[i+1], new_update[i]
        if is_ordered(new_update):
            total_2 += int(new_update[floor((len(new_update) / 2))])
            break


print(total_2)
