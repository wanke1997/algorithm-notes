from typing import Tuple, Set, List, Dict
import heapq
import time


class Kruskal:
    def __init__(self, edges: List[Tuple[str, str, int]]) -> None:
        self.edges = edges
        self.V = self.build_V()
        self.V_sets = {v: set(v) for v in self.V}
        self.rank = {v: 0 for v in self.V}
        self.parent = {v: v for v in self.V}

    def build_V(self) -> Set[str]:
        V: Set[str] = set()
        for start, end, _ in self.edges:
            V.add(start)
            V.add(end)
        return V

    def union(self, start: str, end: str) -> None:
        # get union set
        union_set = self.V_sets[start] | self.V_sets[end]
        # update union set
        for v, V_set in self.V_sets.items():
            if start in V_set or end in V_set:
                self.V_sets[v] = union_set

    def union_adv(self, start: str, end: str) -> None:
        parent_start = self.find(start)
        parent_end = self.find(end)
        if parent_end == parent_start:
            return
        else:
            if self.rank[parent_start] < self.rank[parent_end]:
                self.parent[parent_start] = parent_end
            elif self.rank[parent_start] > self.rank[parent_end]:
                self.parent[parent_end] = parent_start
            else:
                self.parent[parent_end] = parent_start
                self.rank[parent_start] += 1

    def find(self, v: str) -> str:
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def algorithm(self) -> List[Tuple[str, str, int]]:
        heap = [(distance, start, end) for start, end, distance in self.edges]
        heapq.heapify(heap)
        answer = []
        while heap:
            distance, start, end = heapq.heappop(heap)
            # if self.V_sets[start] != self.V_sets[end]:
            #     self.union(start, end)
            #     answer.append((start, end, distance))
            if self.find(start) != self.find(end):
                self.union_adv(start, end)
                answer.append((start, end, distance))
        return answer


if __name__ == "__main__":
    edges = [
        ("a", "b", 4),
        ("a", "h", 8),
        ("b", "h", 11),
        ("b", "c", 8),
        ("h", "i", 7),
        ("h", "g", 1),
        ("i", "g", 6),
        ("i", "c", 2),
        ("c", "f", 4),
        ("g", "f", 2),
        ("d", "f", 14),
        ("c", "d", 7),
        ("d", "e", 9),
        ("e", "f", 10),
    ]
    kruskal = Kruskal(edges)
    ans = kruskal.algorithm()
    print(ans)
