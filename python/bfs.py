from typing import List, Dict
from collections import deque

class bfsClass:
    def __init__(self) -> None:
        self.graph_no_cycle = [[1, 2, 4], [3], [3], [], [1, 2]]
        self.directed_graph = [[1, 2, 3], [3, 4, 5], [4, 5], [5, 6], [6, 7], [7], [7], []]
        self.graph_no_cycle_edge_case = [[1], [0, 2], [1]]
        self.graph_with_cycle = [[1, 2], [3], [3], [4], [0, 2]]
        self.trace = []

    def bfs_basic(self, graph: List[List[int]]) -> None:
        self.trace.clear()
        visited = [False] * len(graph)
        queue = deque()
        # start from node 0
        queue.append(0)
        visited[0] = True

        while queue:
            cur = queue.popleft()
            self.trace.append(cur)
            for adj in graph[cur]:
                if not visited[adj]:
                    # Important:
                    # set as visited while adding to queue prevents repetition in queue
                    queue.append(adj)
                    # print("queue: {}".format(queue))
                    visited[adj] = True

    def get_in_degrees(self, graph: List[List[int]]) -> Dict[int, int]:
        in_degree = {}
        # important: firstly set ALL points as zero, which prevents element loss
        for index in range(len(graph)):
            in_degree[index] = 0
        for adjs in graph:
            for adj in adjs:
                in_degree[adj] = in_degree.get(adj,0) + 1
        return in_degree

    def topological(self, graph: List[List[int]]) -> List[int]:
        res = []
        in_degree = self.get_in_degrees(graph)
        queue = deque()
        visited = [False] * len(graph)
        # firstly add all qualified points to the queue
        for idx, value in in_degree.items():
            if value == 0:
                queue.append(idx)

        while queue:
            cur = queue.popleft()
            res.append(cur)
            visited[cur] = True
            for adj in graph[cur]:
                if visited[adj]:
                    continue
                in_degree[adj] -= 1
                # don't forget this line!
                if in_degree[adj] == 0:
                    queue.append(adj)

        return res


if __name__ == "__main__":
    instance = bfsClass()
    instance.bfs_basic(instance.graph_no_cycle)
    print(instance.trace)  # [0, 1, 2, 4, 3]
    instance.bfs_basic(instance.graph_with_cycle)
    print(instance.trace)  # [0, 1, 2, 3, 4]
    print(instance.topological(instance.directed_graph))  # [0, 1, 2, 3, 4, 5, 6, 7]
