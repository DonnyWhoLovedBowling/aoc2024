from copy import deepcopy as dc
from collections import defaultdict

def add_vecs(v1, v2):
    return v1[0]+v2[0], v1[1]+v2[1]

def in_range(v):
    global lines
    return (0 <= v[0] < len(lines)) and (0 <= v[1] < len(lines[v[0]]))

def get_val(v):
    global lines
    if lines[v[0]][v[1]].isnumeric():
        return lines[v[0]][v[1]]
    else:
        return '999'


if __name__ == '__main__':
    in_file = open("../data/ex10.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    trailheads = [(i, j) for i, sublist in enumerate(lines) for j, value in enumerate(sublist) if value == '0']
    ans1, ans2 = 0, 0
    for t in trailheads:
        path = [t]
        nines = set()
        path_dict = defaultdict(list)
        new_paths = [[t]]
        while len(new_paths) > 0:
            these_paths = dc(new_paths)
            new_paths = []
            for path in these_paths:
                pivot = path[-1]
                if get_val(pivot) == '9':
                    continue
                for delta in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    p = add_vecs(pivot, delta)
                    if not in_range(p):
                        continue
                    if p in path:
                        continue
                    if int(get_val(p)) - int(get_val(pivot)) != 1:
                        continue
                    if get_val(p) == '9':
                        new_paths.append(path + [p])
                        nines.add(p)
                        path_dict[t].append(path + [p])
                    else:
                        new_paths.append(path + [p])

        ans1 += len(nines)
        ans2 += len(path_dict[t])


    print(ans1)
    print(ans2)
    exit(0)
