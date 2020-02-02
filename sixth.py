import networkx as nx
from utility import Utility


def create_graph(file):
    g = nx.Graph()
    for line in Utility.read_linestxt(file):
        u = line.split(')')[0]
        v = line.split(')')[1]
        g.add_node(u)
        g.add_node(v)
        g.add_edge(u, v)
    return g


f = open("sixth.txt", "r")
graph = create_graph(f)
first = 0

for node in graph.nodes:
    first += nx.shortest_path_length(graph, node, "COM")

second = nx.shortest_path_length(graph, "YOU", "SAN") - 2

Utility.print_solution(first, second)
