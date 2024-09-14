from typing import Dict, Set, List

"""
This is Tarjan's Algorithm implementation to find all articulation points in an undirected graph
"""

class APFinder:
    def __init__(self, graph: Dict[int, Set[int]]) -> None:
        self.graph = graph
        self.n = len(self.graph)
        self.visited = [False] * self.n
        self.dist = [-1] * self.n
        self.low = [-1] * self.n
        self.ap = [False] * self.n
        self.time = 0

    def _find(self, cur: int, prev: int) -> None:
        self.visited[cur] = True
        self.dist[cur] = self.low[cur] = self.time
        self.time += 1
        children = 0
        for adj in self.graph[cur]:
            if adj == prev:
                continue
            elif not self.visited[adj]:
                children += 1
                self._find(adj, cur)
                # check case 2: if one of its children v has the property such that no vertex in the subtree
                # rooted with v has a back edge to one of the ancestors in DFS tree of current node u, the node u
                # is a AP
                if prev != -1 and self.low[adj] >= self.dist[cur]:
                    self.ap[cur] = True
                self.low[cur] = min(self.low[cur], self.low[adj])
            else:
                self.low[cur] = min(self.low[cur], self.dist[adj])
        # check case 1: if the current node u is root node, and the number of children is >= 2, it is AP
        if prev == -1 and children >= 2:
            self.ap[cur] = True

    def find(self) -> None:
        for cur in range(self.n):
            if not self.visited[cur]:
                self._find(cur, -1)

    def get_ans(self) -> List[int]:
        res = []
        for i in range(self.n):
            if self.ap[i]:
                res.append(i)
        return res


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
    ap_finder = APFinder(graph)
    ap_finder.find()
    res = ap_finder.get_ans()
    print(res)
    print("debug dist:", ap_finder.dist)
    print("debug low:", ap_finder.low)
