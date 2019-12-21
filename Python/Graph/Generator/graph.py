import random
import numpy as np


def gen_random_simple_graph(num_vertices, num_edges, dimension=2):
    vertices = gen_random_vertices(num_vertices, dimension)
    edges = gen_random_edges(vertices, num_edges)
    return vertices, edges


def gen_random_vertices(num_vertices, dimension):
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
    adj_list = {}
    for edge in edges:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = {edge[1]}
        else:
            adj_list[edge[0]].add(edge[1])
    return adj_list


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_matrix = self.to_adjacency_matrix()
        self.adjacency_list = gen_adjacency_list(self.edges)

    def to_adjacency_matrix(self):
        num_v = len(self.vertices)
        matrix = np.zeros(num_v ** 2).reshape((num_v, num_v))
        for edge in self.edges:
            matrix[edge[0], edge[1]] = 1
            matrix[edge[1], edge[0]] = 1
        self.adjacency_matrix = matrix
        return matrix

    def to_adjacency_list(self):
        adj_list = {}
        for edge in self.edges:
            if edge[0] not in adj_list:
                adj_list[edge[0]] = {edge[1]}
            else:
                adj_list[edge[0]].add(edge[1])
        self.adjacency_list = adj_list
        return adj_list


