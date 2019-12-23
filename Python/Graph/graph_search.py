from graph import *


class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self):
        raise NotImplementedError


class BFS(GraphSearch):
    def __init__(self, graph):
        super().__init__(graph)
        self.BFS_tree = None

    def search(self):
        pass


class DFS(GraphSearch):
    def __init__(self, graph):
        super().__init__(graph)

    def search(self):
        pass
