import unittest
import heapq
import random
from typing import Tuple, Set, Dict


"""
Please implement you Dijkstra Algorithm here!
"""
def my_algorithm(graph: Dict[int, Set[Tuple[int, int]]], start: int, end: int) -> int:
    # graph is [start, Set[[end, weight]]], the return value is shortest distance between start and end
    pass


class TestDijkstraAlgorithm(unittest.TestCase):
    def dijkstra(self, graph, start, end):
        distances = {vertex: 10**9 for vertex in graph}
        distances[start] = 0
        priority_queue = [(0, start)]
        
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return distances[end]

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
        
        return graph

    def test_shortest_distance(self):
        graph = self.generate_weighted_graph(5, 7)
        start = 0
        end = 4
        ref_answer = self.dijkstra(graph, start, end)
        my_answer = my_algorithm(graph, start, end)
        self.assertIsNotNone(ref_answer)
        self.assertIsNotNone(my_answer)
        assert ref_answer == my_answer
        print("Generated Weighted Graph:", graph)
        print(f"Shortest distance from vertex {start} to vertex {end}:", ref_answer)

if __name__ == '__main__':
    unittest.main()
