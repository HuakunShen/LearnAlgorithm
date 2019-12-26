from graph import *
import random


# class Vertex(Vertex):
#     def __init__(self):
#         self.d = float("inf")
#         self.parent = 1
#
#     def get_distance(self):
#         return self.d
#
#     def get_parent(self):
#         return self.parent
#
#     def set_distance(self, distance):
#         self.d = distance
#
#     def set_parent(self, parent):
#         self.parent = parent


class SingleSourceShortestPath(WeightedGraph):
    def __init__(self, vertices, edges, weights, source_index):
        super().__init__(vertices, edges, weights)
        self.source = self.vertices[source_index]
        self.initialize_single_source()

    def initialize_single_source(self):
        for vertex in self.vertices:
            vertex.d = float("inf")
            vertex.parent = None
        self.source.d = 0

    def relax(self, u: int, v: int):
        if (u, v) not in self.weight_dict:
            raise Exception
        if self.vertices[v].d > self.vertices[u].d + self.weight_dict[(u, v)]:
            self.vertices[v].d = self.vertices[u].d + self.weight_dict[(u, v)]
            self.vertices[v].parent = self.vertices[u]

    def bellman_ford(self):
        self.initialize_single_source()
        for _ in range(len(self.vertices) - 1):
            for edge in self.edges:
                self.relax(edge.edge[0], edge.edge[1])
        for edge in self.edges:
            u = edge.edge[0]
            v = edge.edge[1]
            if self.vertices[v].d > self.vertices[u].d + self.weight_dict[(u, v)]:
                return False
        return True


vertices, edges = gen_random_simple_graph(5, 5)
graph = SingleSourceShortestPath(vertices, edges, [random.randint(1, 10) for i in range(5)], 0)
