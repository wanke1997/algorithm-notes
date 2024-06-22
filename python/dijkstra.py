from typing import Dict, List, Tuple
import heapq

# dijkstra algorithm does not work a graph with negative loops

class Dijkstra:
    def __init__(self, edges: List[Tuple[int, int, int]], num_nodes: int) -> None:
        self.edges = edges
        self.num_nodes = num_nodes
        self.graph = self.build_graph()

    def build_graph(self) -> Dict[int, List[Tuple[int, int]]]:
        graph: Dict[int, List[Tuple[int, int]]] = dict()
        for i in range(self.num_nodes):
            graph[i] = []
        for start, end, weight in self.edges:
            graph[start].append((end, weight))
        return graph

    def shortest_path(self, start: int, end: int) -> Tuple[str, int]:
        visited = [False] * len(self.graph)
        prev = [-1] * len(self.graph)
        distances = [10**9] * len(self.graph)
        heap = []
        heapq.heapify(heap)

        # initialize
        distances[start] = 0
        heapq.heappush(heap, (0, start))

        while heap:
            cur_d, cur_idx = heapq.heappop(heap)
            # retrieve the nearest node
            visited[cur_idx] = True
            if cur_idx == end:
                break

            for adj, value in self.graph[cur_idx]:
                next_d = cur_d + value
                # skip visited nodes
                if visited[adj]:
                    continue
                # add new nearest distance and point to heap
                if next_d < distances[adj]:
                    # 注意：在加进的时候更新distance和parent
                    distances[adj] = next_d
                    prev[adj] = cur_idx
                    heapq.heappush(heap, (next_d, adj))
                    
        answer = str(end)
        cur = end
        while cur!=-1:
            cur = prev[cur]
            if cur != -1:
                answer = "{}->{}".format(cur, answer)
        
        return answer, distances[end]


if __name__ == "__main__":
    num_nodes = 9
    edges = [
        (0, 1, 4),
        (0, 7, 8),
        (1, 0, 4),
        (1, 2, 8),
        (1, 7, 11),
        (2, 1, 8),
        (2, 3, 7),
        (2, 5, 4),
        (2, 8, 2),
        (3, 2, 7),
        (3, 4, 9),
        (3, 5, 14),
        (4, 3, 9),
        (4, 5, 10),
        (5, 2, 4),
        (5, 3, 14),
        (5, 4, 10),
        (5, 6, 2),
        (6, 5, 2),
        (6, 7, 1),
        (6, 8, 6),
        (7, 0, 8),
        (7, 1, 11),
        (7, 6, 1),
        (7, 8, 7),
        (8, 2, 2),
        (8, 6, 6),
        (8, 7, 7),
    ]
    instance = Dijkstra(edges, num_nodes)
    start = 1
    end = 1
    path, distance = instance.shortest_path(start, end)
    print("path:{}, distance:{}".format(path, distance))
