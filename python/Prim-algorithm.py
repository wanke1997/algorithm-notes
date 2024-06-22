from typing import List, Tuple, Dict, Set, Optional
import heapq


class Prim:
    def __init__(self, edges: List[Tuple[str, str, int]]) -> None:
        self.edges = edges
        self.vertex_set = self.build_vertex()
        self.graph = self.build_graph()

    def build_vertex(self) -> Set[str]:
        vertex: Set[str] = set()
        for start, end, _ in self.edges:
            vertex.add(start)
            vertex.add(end)
        return vertex

    def build_graph(self) -> Dict[str, Set[Tuple[str, int]]]:
        graph: Dict[str, Set[Tuple[str, int]]] = {v: set() for v in self.vertex_set}
        for start, end, weight in self.edges:
            graph[start].add((end, weight))
            graph[end].add((start, weight))
        return graph

    def algorithm(self, start: str) -> List[Tuple[Optional[str], str, int]]:
        parent: Dict[str, Optional[str]] = {v: None for v in self.vertex_set}
        distance: Dict[str, int] = {v: 10 ** 9 for v in self.vertex_set}
        visited: Dict[str, bool] = {v: False for v in self.vertex_set}
        answer: List[Tuple[Optional[str], str, int]] = []
        distance[start] = 0

        # 与Dijkstra算法区别
        # 区别1: Prim将所有节点加入heap，而Dijkstra只加入第一个
        heap = [(distance[v], v, parent[v]) for v in self.vertex_set]
        heapq.heapify(heap)

        while heap:
            d, v, p = heapq.heappop(heap)
            if d > 0 and not visited[v]:
                answer.append((p, v, d))
            visited[v] = True
            for adj, weight in self.graph[v]:
                if visited[adj]:
                    continue
                if weight < distance[adj]:
                    # 注意：在加进的时候更新distance和parent
                    # 区别2: Prim的distance表示vertex离树的最近距离，而Dijkstra表示离起点的距离
                    distance[adj] = weight
                    parent[adj] = v
                    heapq.heappush(heap, (weight, adj, v))

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
    prim = Prim(edges)
    ans = prim.algorithm(start="a")
    print(ans)
