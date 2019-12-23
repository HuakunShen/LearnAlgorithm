from graph import *


class Vertex:
    def __init__(self):
        self.d = float("inf")
        self.parent = None

    def get_distance(self):
        return self.d

    def get_parent(self):
        return self.parent

    def set_distance(self, distance):
        self.d = distance

    def set_parent(self, parent):
        self.parent = parent


class SingleSourceShortestPath:
    def __init__(self, weighted_graph):
        self.graph = weighted_graph




