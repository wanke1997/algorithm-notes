from typing import List, Tuple, Dict

# bellman-ford works for a graph who has negative loops

class BellmanFord:
    def __init__(self, edges: List[Tuple[int, int, int]], n: int) -> None:
        self.n = n
        self.edges = edges
        self.distances = [10**9 for i in range(self.n)]

    def relax(self, start: int, end: int, weight: int) -> None:
        if self.distances[end] > self.distances[start] + weight:
            self.distances[end] = self.distances[start] + weight

    def algorithm(self, s: int) -> bool:
        self.distances[s] = 0
        # relaxation for n-1 loops
        for _ in range(self.n - 1):
            # relaxation for all edges
            for start, end, weight in self.edges:
                self.relax(start, end, weight)
        # determine if there is any negative loop
        for start, end, weight in self.edges:
            if self.distances[end] > self.distances[start] + weight:
                return True
        return False


if __name__ == "__main__":
    edges = [
        (0, 1, 6),
        (4, 2, -3),
        (1, 2, 5),
        (4, 3, 9),
        (2, 1, -2),
        (1, 4, 8),
        (3, 2, 7),
        (0, 4, 7),
        (1, 3, -4),
        (3, 0, 2),
    ]
    n = 5
    instance = BellmanFord(edges, n)
    res = instance.algorithm(0)
    print(instance.distances)
    print(res)
