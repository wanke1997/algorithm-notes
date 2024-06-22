from typing import List


class dfsClass:
    def __init__(self) -> None:
        self.graph_no_cycle = [[1, 2, 4], [3], [3], [], [1, 2]]
        self.graph_no_cycle_edge_case = [[1], [0, 2], [1]]
        self.graph_with_cycle = [[1, 2], [3], [3], [4], [0, 2]]
        self.trace = []

    def dfs(self, cur: int, visited: List[bool], graph: List[List[int]]) -> None:
        if visited[cur]:
            return
        else:
            self.trace.append(cur)
            visited[cur] = True
            for adj in graph[cur]:
                self.dfs(adj, visited, graph)

    def has_cycle(self, cur: int, parent: int, color: List[int], graph: List[List[int]]) -> bool:
        # 比普通dfs多了一个parent参数，用于避免往回找
        if color[cur] == 2:
            return False
        elif color[cur] == 1:
            return True
        else:
            color[cur] = 1
            for adj in graph[cur]:
                # 易错点：一定要判断下一个点是否是parent，否则会出错
                if adj == parent:
                    continue
                if self.has_cycle(adj, cur, color, graph):
                    return True
            color[cur] = 2
            return False


if __name__ == "__main__":
    instance = dfsClass()
    instance.dfs(0, [False] * len(instance.graph_no_cycle), instance.graph_no_cycle)
    print(instance.trace)
    print(instance.has_cycle(0, -1, [0] * len(instance.graph_no_cycle), instance.graph_no_cycle))  # False
    print(
        instance.has_cycle(0, -1, [0] * len(instance.graph_no_cycle_edge_case), instance.graph_no_cycle_edge_case)
    )  # False
    print(instance.has_cycle(0, -1, [0] * len(instance.graph_with_cycle), instance.graph_with_cycle))  # True
