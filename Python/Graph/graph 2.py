import random
import numpy as np

"""
Implementation Ideas:
- Undirected graph: every edge is bidirectional, add 2 edges for 2 vertices

"""


def gen_random_simple_graph(num_vertices, num_edges, dimension=2):
    vertices = gen_random_vertices_coordinate(num_vertices, dimension)
    edges = gen_random_edges(vertices, num_edges)
    return vertices, edges


def gen_random_vertices_coordinate(num_vertices, dimension):
    """
    :param num_vertices: number of vertices needed for a graph
    :param dimension: dimension of each vertex, d-dimension vertex is a d-length tuple
    :return: a list of tuple of length=num_vertices
    """
    vertices = []
    i = 0
    while i < num_vertices:
        vertex = [random.randint(0, num_vertices) for d in range(dimension)]
        vertex = tuple(vertex)
        if not vertex in vertices:
            vertices.append(vertex)
            i += 1
    vertices.sort()
    return vertices


def gen_random_edges(vertices, num_edges):
    """

    :param vertices: a list of tuple
    :param num_edges: number of edges needed for a graph
    :return: a list of tuple (size 2) of length num_edges, a tuple contains 2 indices representing 2 vertices in the
    vertex list
    """
    edges = []
    while num_edges > 0:
        # randomly choose 1 vertex as 1 end
        first_v_index = random.randint(0, len(vertices) - 1)
        second_v_index = randint_without(0, len(vertices) - 1, first_v_index)
        if (first_v_index, second_v_index) not in edges and (second_v_index, first_v_index) not in edges:
            edges.append((first_v_index, second_v_index))
            num_edges -= 1
    return edges


def randint_without(start, end, exception):
    """
    a helper, improved based on random.randint.
    generate a random integer and make sure it's not the exception
    :param start: lower bound
    :param end: upper bound
    :param exception: don't want this integer
    :return: a random integer between start and end, but not exception
    """
    index = random.randint(start, end)
    while index == exception:
        index = random.randint(start, end)
    return index


def gen_adjacency_matrix(vertices, edges):
    """
    :param vertices: a list of vertices (tuples)
    :param edges: a list of edges (tuples), matching indices of vertices
    :return: a 2D array, matrix, representing the graph, matrix[x][y] == 1 means (x, y) is an edge, 0 otherwise
    """
    num_v = len(vertices)
    matrix = np.zeros(num_v ** 2).reshape((num_v, num_v))
    for edge in edges:
        matrix[edge[0], edge[1]] = 1
        matrix[edge[1], edge[0]] = 1
    return matrix


def gen_adjacency_list(edges):
    """
    :param edges: a list of edges (tuples)
    :return: A adjacency list representation of a graph given edges. A dictionary, key is vertex, value is a set of vertices
        which are reachable from the key vertex
    """
    adj_list = {}
    for edge in edges:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = {edge[1]}
        else:
            adj_list[edge[0]].add(edge[1])
    return adj_list


def euclidean_distance(vertex1, vertex2):
    """
    :param vertex1: a tuple representing a vertex
    :param vertex2: a tuple representing a vertex
    :return: a norm/euclidean distance, a scalar
    """
    return np.linalg.norm(np.array(vertex1) - np.array(vertex2))


class Vertex:
    def __init__(self, coordinate):
        self.coordinate = coordinate


class Edge:
    def __init__(self, edge):
        self.edge = edge

    def get_tuple(self):
        return self.edge

    def get_start(self):
        return self.edge[0]

    def get_end(self):
        return self.edge[1]

    def set_tuple(self, edge):
        self.edge = edge

    def get_reversed_tuple(self):
        return self.edge[1], self.edge[0]


class Graph:
    def __init__(self, vertices, edges, dimension=2, undirected=False):
        assert len(vertices) > 0
        for vertex in vertices:
            assert len(vertex) == dimension
        self.vertices = []
        for vertex in vertices:
            self.vertices.append(Vertex(vertex))
        self.undirected = undirected
        # setup edges
        self.edges = []
        for edge in edges:
            self.edges.append(Edge(edge))
        if undirected:  # add bidirectional edges
            for edge in self.edges:
                reversed_edge_tuple = edge.get_reversed_tuple()
                if reversed_edge_tuple not in self.edges:
                    self.edges.append(Edge(reversed_edge_tuple))
        self.dimension = dimension
        self.adjacency_matrix = self.get_adjacency_matrix()
        self.adjacency_list = self.get_adjacency_list()

    def get_adjacency_matrix(self):
        """
        :return: a adjacency matrix representation of graph, consisting of 0 and 1's. 1 at matrix[row][col] means (u,
        v) is an edge
        """
        num_v = len(self.vertices)
        matrix = np.zeros(num_v ** 2).reshape((num_v, num_v))
        for edge in self.edges:
            matrix[edge[0], edge[1]] = 1
            matrix[edge[1], edge[0]] = 1
        return matrix

    def get_adjacency_list(self):
        """
        :return: an adjacency list representation of graph. A dictionary, key is vertex, value is a set of vertices
        which are reachable from the key vertex
        """
        adj_list = {}
        for edge in self.edges:
            if edge[0] not in adj_list:
                adj_list[edge[0]] = {edge[1]}
            else:
                adj_list[edge[0]].add(edge[1])
        return adj_list

    def adjacency_list_tostring(self):
        self.update_representation()
        result = ""
        for key_vertex in self.get_adjacency_list:
            result += str(key_vertex) + ": " + str(self.get_adjacency_list[key_vertex]) + "\n"

        return result

    def add_vertex(self, vertex):
        """
        add a vertex to graph
        :param vertex: a tuple of length self.dimension
        :return: all vertices, a list of tuple
        """
        if len(vertex) != self.dimension:
            print("Adding vertex " + str(vertex) + " dimension incorrect, dimension should be " + str(self.dimension))
            return -1
        self.vertices.append(vertex)
        self.update_representation()
        return self.vertices

    def add_edge(self, edge):
        """
        add an edge to graph
        :param edge: a tuple of 2 integers (vertices of graph), representing the connection between 2 edges
        :return: all edges, a list of tuple
        """
        if len(edge) != 2 or type(edge[0]) is not int or type(edge[1]) is not int:
            print("input incorrect\ninput: " + str(edge) + "\ncorrect input type is (int, int)")
        if edge not in self.edges:
            self.edges.append(edge)
        if self.undirected and (edge[1], edge[0]) not in self.edges:  # add bidirectional edge
            self.edges.append((edge[1], edge[0]))
        self.update_representation()
        return self.edges

    def update_representation(self):
        self.adjacency_matrix = self.get_adjacency_matrix()
        self.adjacency_list = self.get_adjacency_list()


class CompleteGraph(Graph):
    """
    A complete graph has edge between every 2 vertices, and always undirected
    """

    def __init__(self, vertices, dimension=2, undirected=True):
        # add all edges
        vertex_indices = range(len(vertices))
        edges = [(i, j) for i in vertex_indices for j in vertex_indices]
        super().__init__(vertices, edges, dimension=dimension, undirected=undirected)

    def add_vertex(self, vertex):
        assert len(vertex) == self.dimension
        self.vertices.append(vertex)
        new_vertex_index = len(self.vertices) - 1
        for i in range(len(self.vertices) - 1):
            if (i, new_vertex_index) not in self.vertices:
                self.vertices.append((i, new_vertex_index))
            if (new_vertex_index, i) not in self.vertices:
                self.vertices.append((new_vertex_index, i))


class WeightedGraph(Graph):
    def __init__(self, vertices, edges, weights, dimension=2, undirected=False, negative_weight=False):
        super().__init__(vertices, edges, dimension=dimension, undirected=undirected)
        self.negative_weight = negative_weight
        assert len(weights) == len(edges)  # every edge has a weight, 1-to-1
        if not negative_weight:  # if negative weight is not allowed, make sure that there is really no negative weight
            for weight in weights:
                assert weight > 0
        self.weights = weights

    def add_edge(self, edge, weight):
        if len(edge) != 2 or type(edge[0]) is not int or type(edge[1]) is not int:
            raise Exception("Invalid input\ninput: " + str(edge) + "\ncorrect input type is (int, int)")
        if edge[0] >= len(self.vertices) or edge[1] >= len(self.vertices):
            raise Exception("edge index out of bound, doesn't represent a vertex")
        if edge not in self.edges:
            self.edges.append(edge)
            self.weights.append(weight)
            if self.undirected and (edge[1], edge[0]) not in self.edges:
                self.edges.append((edge[1], edge[0]))  # add an extra edge for undirected graph
                self.weights.append(weight)  # add an extra weight for the extra edge
        return self.edges, self.weights


class EuclideanDistanceWeightedGraph(WeightedGraph):
    def __init__(self, vertices, edges, dimension=2, undirected=False, negative_weight=False):
        weights = []
        for edge in self.edges:
            vertex1 = self.vertices[edge[0]]
            vertex2 = self.vertices[edge[1]]
            distance = euclidean_distance(vertex1, vertex2)
            weights.append(distance)
        super().__init__(vertices, edges, weights=weights, dimension=dimension, undirected=undirected,
                         negative_weight=negative_weight)

    def add_edge(self, edge):
        if len(edge) != 2 or type(edge[0]) is not int or type(edge[1]) is not int:
            raise Exception("Invalid input\ninput: " + str(edge) + "\ncorrect input type is (int, int)")
        if edge[0] >= len(self.vertices) or edge[1] >= len(self.vertices):
            raise Exception("edge index out of bound, doesn't represent a vertex")
        if edge not in self.edges:
            vertex1 = self.vertices[edge[0]]
            vertex2 = self.vertices[edge[1]]
            weight = euclidean_distance(vertex1, vertex2)
            self.edges.append(edge)
            self.weights.append(weight)
            if self.undirected and (edge[1], edge[0]) not in self.edges:
                self.edges.append((edge[1], edge[0]))  # add an extra edge for undirected graph
                self.weights.append(weight)  # add an extra weight for the extra edge
        return self.edges, self.weights
