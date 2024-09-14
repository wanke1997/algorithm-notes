"""
This is Kosaraju's Algorithm implementation to find all strong components in a directed graph

It requires two DFS running. 
1> The first one is to mark nodes with numbers with postorder traversal using initial graph G1. 
2> The second one is to find all strong components from greatest number node to smallest number node using reversed graph G2. 

"""

from typing import Dict, Set, List, Tuple


class SCCFinder:
    def __init__(self, n: int, graph: Dict[int, Set[int]], r_graph: Dict[int, Set[int]]) -> None:
        self.graph = graph
        self.r_graph = r_graph
        self.n = n
        self.visited = [False] * self.n
        self.nums = [-1] * self.n
        self.sc = [-1] * self.n
        self.cur_sc = 0
        self.idx = 0

    def _dfs1(self, cur: int) -> None:
        self.visited[cur] = True
        for adj in self.graph[cur]:
            if not self.visited[adj]:
                self._dfs1(adj)
        self.nums[self.idx] = cur
        self.idx += 1

    def _dfs2(self, cur: int) -> None:
        self.sc[cur] = self.cur_sc
        for adj in self.r_graph[cur]:
            if self.sc[adj] == -1:
                self._dfs2(adj)

    def kosaraju(self) -> Dict[int, List[int]]:
        # 1st dfs
        for node in range(self.n):
            if not self.visited[node]:
                self._dfs1(node)

        # 2nd dfs
        for i in range(self.n - 1, -1, -1):
            node = self.nums[i]
            if self.sc[node] == -1:
                self._dfs2(node)
                self.cur_sc += 1

        # get final results
        res = {}
        for idx, val in enumerate(self.sc):
            if val not in res:
                res[val] = []
            res[val].append(idx)
        ans = []
        for val in res.values():
            ans.append(val)
        return ans


if __name__ == "__main__":

    def build_graph(n: int, edges: List[List[int]]) -> Tuple[Dict[int, Set[int]], Dict[int, Set[int]]]:
        graph = {i: set() for i in range(n)}
        r_graph = {i: set() for i in range(n)}
        for s, e in edges:
            graph[s].add(e)
            r_graph[e].add(s)

        return graph, r_graph

    n = 5
    edges = [[0, 3], [1, 3], [2, 4], [3, 2], [4, 3]]
    graph, r_graph = build_graph(n, edges)
    instance = SCCFinder(n, graph, r_graph)
    res = instance.kosaraju()
    print(res)
