from networkx import Graph, isolates, draw_networkx
from itertools import combinations

from matplotlib import pyplot as plt
import matplotlib
from networkx.algorithms.clique import find_cliques

matplotlib.use("TkAgg")


if __name__ == '__main__':
    in_file = open("../data/ex23.txt")
    lines = [l.replace('\\n', '').strip() for l in in_file.readlines()]
    full_graph = Graph()
    for line in lines:
        nodes = line.split('-')
        node1 = nodes[0]
        node2 = nodes[1]
        if node1 not in full_graph.nodes():
            full_graph.add_node(node1)
        if node2 not in full_graph.nodes():
            full_graph.add_node(node2)
        # if 't' == node2[0] or 't' == node1[0]:
        full_graph.add_edge(node1, node2)
        # full_graph.add_edge(node2, node1)

    connected_nodes = set(full_graph.nodes()).difference(set(isolates(full_graph)))
    ans_1 = 0
    all_combs = set(filter(lambda x: x[0][0] == 't' or x[1][0] == 't' or x[2][0] == 't' ,
                       combinations(connected_nodes, 3)))
    for i, comb in enumerate(all_combs):
        if i % 100000 == 0:
            print(i, len(all_combs))
        subgraph = full_graph.subgraph(comb)
        if len(subgraph.edges()) == 3:
            ans_1 += 1
    print(ans_1)

    cliques = sorted(find_cliques(full_graph), key=len)
    largest_clique = sorted(cliques[-1])
    print(','.join(largest_clique))
