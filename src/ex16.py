from collections import defaultdict
import heapq

def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def subtract(v1, v2):
    return v1[0]-v2[0], v1[1]-v2[1]

def calc_all_shortest_paths():
    global graph, start, end, paths

    visited = dict()
    queue = []
    heapq.heappush(queue, (0, [start]))
    shortest_path_score = 9999999
    while queue:
        item = heapq.heappop(queue)
        _path = item[1]
        node = _path[-1]
        score = item[0]
        if score > shortest_path_score:
            continue

        if len(_path) == 1:
            _dir = (1, 0)
        else:
            _dir = subtract(_path[-1], _path[-2])
        do_it = True
        if (_dir, node) in visited:
            do_it = visited[(_dir, node)] >= score
        if do_it:
            neighbours = graph[node]
            for neighbour in neighbours:
                if neighbour in _path:
                    continue
                new_path = list(_path)
                new_path.append(neighbour)
                new_score = calc_score(new_path)
                heapq.heappush(queue, (new_score, new_path))

                if neighbour == end:
                    paths.append(new_path)
                    shortest_path_score = new_score
            visited[(_dir, node)] = score

def calc_score(_path):
    if len(_path) > 1:
        direction = (1, 0)
        score = 0
        for i in range(1, len(_path)):
            p2 = _path[i]
            p1 = _path[i - 1]
            new_direction = subtract(p2, p1)
            score += 1
            if new_direction != direction:
                score += 1000
            direction = new_direction
        return score
    else:
        print('? ', _path)


if __name__ == '__main__':
    in_file = open("../data/ex16.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    vertices = set()
    start = ()
    end = ()
    graph = defaultdict(set)
    paths = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == '.':
                vertices.add((j, i))
            elif c == 'S':
                start = (j, i)
                vertices.add((j, i))
            elif c == 'E':
                end = (j, i)
                vertices.add((j, i))
    for v in vertices:
        for p in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            np = add_vecs(v, p)
            if np in vertices:
                graph[v].add(np)
                graph[np].add(v)

    calc_all_shortest_paths()
    shortest = paths[0]
    print(calc_score(shortest))
    full_set = set()
    for _path in paths:
        full_set.update(set(_path))
    print(len(full_set))


