from collections import defaultdict
import heapq

def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def calc_all_shortest_paths():
    global graph, start, end

    visited = set()
    queue = []
    heapq.heappush(queue, (0, [start]))
    while queue:
        item = heapq.heappop(queue)
        _path = item[1]
        node = _path[-1]

        if node not in visited and node in graph.keys():
            _neighbours = graph[node]
            for neighbour in _neighbours:
                if neighbour in _path:
                    continue
                new_path = list(_path)
                new_path.append(neighbour)
                heapq.heappush(queue, (len(new_path), new_path))

                if neighbour == end:
                    return len(new_path)
            visited.add(node)


if __name__ == '__main__':
    in_file = open("../data/ex18.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    blocks = set()
    size = 100
    start = (0, 0)
    end = (size-1, size-1)
    for i, line in enumerate(lines):
        blocks.add(tuple([int(n) for n in line.split(',')]))
        if len(blocks) == 1024:
            break
    print(blocks)
    graph = dict()
    for i in range(size):
        for j in range(size):
            neighbours = list()
            for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n = add_vecs((i, j), delta)
                if n not in blocks and 0 <= n[0] < size and  0 <= n[1] < size:
                    neighbours.append(add_vecs((i, j), delta))
            graph[(i, j)] = neighbours

    print(calc_all_shortest_paths()-1)
