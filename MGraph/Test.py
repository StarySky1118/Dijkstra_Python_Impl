# -*- coding:utf-8 -*-
# for i in range(5):
#     print(i)
from MGraph import MGraph

graph = MGraph(5)
graph.load_example()
graph.print_matrix()

print(graph.shortest_path_dij())


