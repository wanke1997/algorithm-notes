import unittest
import random


# def my_prim_algorithm(graph)

# def my_kruskal_algorithm(graph)



class TestMSTAlgorithm(unittest.TestCase):
    def prim(self, graph):
        # Initialize empty set to store visited vertices
        visited = set()
        # Choose a random start vertex
        start_vertex = random.choice(list(graph.keys()))
        # Initialize MST (Minimum Spanning Tree) with the start vertex
        mst = {start_vertex: set()}
        
        # Loop until all vertices are visited
        while len(visited) < len(graph):
            min_edge = None
            min_weight = float('inf')
            
            # Loop through all vertices in the MST
            for vertex in mst:
                # Loop through all edges of the current vertex
                for neighbor, weight in graph[vertex]:
                    # If the neighbor is not visited and the weight is less than the minimum weight
                    if neighbor not in visited and weight < min_weight:
                        min_edge = (vertex, neighbor)
                        min_weight = weight
            
            # Add the minimum edge to the MST
            if min_edge:
                vertex, neighbor = min_edge
                mst[vertex].add((neighbor, min_weight))
                mst.setdefault(neighbor, set()).add((vertex, min_weight))
                visited.add(neighbor)
        
        return mst

    def generate_weighted_graph(self, num_vertices, num_edges):
        graph = {}
        vertices = set(range(num_vertices))
        for vertex in vertices:
            graph[vertex] = set()
        
        edges = set()
        while len(edges) < num_edges:
            start = random.choice(list(vertices))
            end = random.choice(list(vertices - {start}))
            weight = random.randint(1, 10)
            edge = (start, end)
            if edge not in edges:
                edges.add(edge)
                graph[start].add((end, weight))
                graph[end].add((start, weight))  # Undirected graph
        
        return graph

    def test_minimum_spanning_tree(self):
        graph = self.generate_weighted_graph(5, 7)
        mst = self.prim(graph)
        self.assertIsNotNone(mst)
        print("Generated Weighted Graph:", graph)
        print("Minimum Spanning Tree (MST):", mst)

if __name__ == '__main__':
    unittest.main()
