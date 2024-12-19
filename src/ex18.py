import heapq

def add_vecs(v1, v2, factor=1):
    return v1[0]+(factor*v2[0]), v1[1]+(factor*v2[1])

def create_graph(_blocks):
    global size
    _graph = dict()
    for i in range(size):
        for j in range(size):
            if (i, j) in _blocks:
                continue
            neighbours = list()
            for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n = add_vecs((i, j), delta)
                if n not in _blocks and 0 <= n[0] < size and  0 <= n[1] < size:
                    neighbours.append(add_vecs((i, j), delta))
            _graph[(i, j)] = neighbours
    return _graph

def calc_all_shortest_paths(graph):
    global start, end

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
    return -1


if __name__ == '__main__':
    in_file = open("../data/ex18.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    blocks = set()
    size = 71
    stop_at = 12 if size == 7 else 1024
    start = (0, 0)
    end = (size-1, size-1)
    for i, line in enumerate(lines[0:stop_at]):
        blocks.add(tuple([int(n) for n in line.split(',')]))

    print(calc_all_shortest_paths(create_graph(blocks))-1)

    for i, line in enumerate(lines[stop_at:]):
        if i % 100 == 0:
            print(i, line)
        blocks.add(tuple([int(n) for n in line.split(',')]))
        if calc_all_shortest_paths(create_graph(blocks)) == -1:
            print(line)
            break