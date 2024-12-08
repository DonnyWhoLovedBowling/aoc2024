from collections import defaultdict


def is_in_range(node):
    global border
    in_range = True
    if node[0] < 0 or node[0] >= border:
        in_range = False
    if node[1] < 0 or node[1] >= border:
        in_range = False
    return in_range


def add_nodes(n1, n2, multiplier=1):
    return n1[0] + (multiplier * n2[0]), n1[1] + (multiplier * n2[1])


if __name__ == '__main__':
    in_file = open("../data/ex8.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    antennas = defaultdict(list)
    antinodes = set()
    antinodes_2 = set()
    border = len(lines)

    for i in range(0, border):
        for j in range(0, border):
            if lines[j][i] != '.':
                antennas[lines[j][i]].append((j, i))

    for s in antennas.keys():
        these_antennas = antennas[s]
        for i in range(len(these_antennas)):
            for j in range(i+1, len(these_antennas)):
                a1 = these_antennas[i]
                a2 = these_antennas[j]
                diff = add_nodes(a1, a2, -1)
                antinode = a1
                _iter = 0
                while is_in_range(antinode):
                    antinodes_2.add(antinode)
                    if _iter == 1:
                        antinodes.add(antinode)
                    _iter += 1
                    antinode = add_nodes(a1, diff, _iter)

                _iter = 0
                antinode = a2
                while is_in_range(antinode):
                    antinodes_2.add(antinode)
                    if _iter == 1:
                        antinodes.add(antinode)
                    _iter += 1
                    antinode = add_nodes(a2, diff, -1 * _iter)

    print(len(antinodes))
    print(len(antinodes_2))
