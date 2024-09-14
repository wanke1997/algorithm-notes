from typing import Dict, Set, List

"""
This is Tarjan's Algorithm implementation to find all bridges in an undirected graph
"""


class BridgeFinder:
    def __init__(self, graph: Dict[int, Set[int]]) -> None:
        self.graph = graph
        self.n = len(self.graph)
        self.visited = [False] * self.n
        self.dist = [-1] * self.n
        self.low = [-1] * self.n
        self.time = 0
        self.bridges = []

    def _find(self, cur: int, prev: int) -> None:
        self.visited[cur] = True
        self.dist[cur] = self.low[cur] = self.time
        self.time += 1
        for adj in self.graph[cur]:
            if adj == prev:
                continue
            elif not self.visited[adj]:
                self._find(adj, cur)
                # we only need to check one case: if has at lease one child 'adj' forming a subtree, and all nodes in the subtree don't
                # have any back edges leading to cur or cur's ancester, then edge [cur, adj] is a bridge.
                # Caution: the operation is >, not >= because we don't want any edge pointing to the cur node.
                if self.low[adj] > self.dist[cur]:
                    self.bridges.append([cur, adj])
                self.low[cur] = min(self.low[cur], self.low[adj])
            else:
                self.low[cur] = min(self.low[cur], self.dist[adj])

    def find(self) -> None:
        for cur in range(self.n):
            if not self.visited[cur]:
                self._find(cur, -1)

    def get_ans(self) -> List[List[int]]:
        return self.bridges


if __name__ == "__main__":

    def build_graph(n: int, edges: List[List[int]]) -> Dict[int, Set[int]]:
        graph = {i: set() for i in range(n)}
        for v, w in edges:
            graph[v].add(w)
            graph[w].add(v)
        return graph

    n = 8
    edges = [[0, 1], [0, 2], [0, 7], [2, 3], [3, 4], [3, 5], [3, 6], [2, 6]]
    graph = build_graph(n, edges)
    ap_finder = BridgeFinder(graph)
    ap_finder.find()
    res = ap_finder.get_ans()
    print(res)
    print("debug dist:", ap_finder.dist)
    print("debug low:", ap_finder.low)
