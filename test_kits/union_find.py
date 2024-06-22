import unittest
import random

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

class UnionFindTest(unittest.TestCase):
    def test_union_find(self):
        num_vertices = 5
        num_edges = 7
        
        # Generate a random weighted graph
        graph = self.generate_weighted_graph(num_vertices, num_edges)
        
        # Generate random edges for Union-Find data structure
        edges = self.generate_random_edges(num_vertices, num_edges)
        
        # Test Union-Find data structure
        uf = UnionFind(num_vertices)
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        # Check if the connected components are correct
        for vertex in range(num_vertices):
            self.assertEqual(uf.find(vertex), self.get_expected_root(vertex, edges))

    def generate_weighted_graph(self, num_vertices, num_edges):
        graph = {}
        vertices = set(range(num_vertices))
        for vertex in vertices:
            graph[vertex] = set()
        
        edges = set()
        while len(edges) < num_edges:
            start = random.randint(0, num_vertices - 1)
            end = random.randint(0, num_vertices - 1)
            if start != end:
                weight = random.randint(1, 10)
                edge = (min(start, end), max(start, end), weight)  # Store as (start, end, weight)
                if edge not in edges:
                    edges.add(edge)
                    graph[start].add(end)
                    graph[end].add(start)  # Undirected graph
        
        return graph

    def generate_random_edges(self, num_vertices, num_edges):
        edges = []
        while len(edges) < num_edges:
            start = random.randint(0, num_vertices - 1)
            end = random.randint(0, num_vertices - 1)
            if start != end:
                edges.append((start, end))
        return edges

    def get_expected_root(self, vertex, edges):
        for edge in edges:
            if vertex in edge:
                return min(edge)

if __name__ == '__main__':
    unittest.main()

