class UnionFindAdvanced:
    def __init__(self, n: int) -> None:
        # use dictionary to store parent and rank
        self.rank = {i: 0 for i in range(1, n + 1)}
        self.parent = {i: i for i in range(1, n + 1)}

    def find_set(self, v: int, w: int) -> bool:
        res1 = self.find(v)
        res2 = self.find(w)
        return res1 == res2

    def find(self, v: int) -> int:
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def union(self, v1: int, v2: int) -> None:
        # union the root node of v1 and v2
        # not the v1 and v2 node!
        self._link(self.find(v1), self.find(v2))

    def _link(self, v1: int, v2: int) -> None:
        # link root node v1 and root node v2
        rank1 = self.rank[v1]
        rank2 = self.rank[v2]

        if rank1 > rank2:
            self.parent[v2] = v1
        elif rank1 < rank2:
            self.parent[v1] = v2
        else:
            self.parent[v1] = v2
            self.rank[v2] += 1


if __name__ == "__main__":
    edges = [
        (1, 2),
        (1, 3),
        (2, 3),
        (2, 4),
        (5, 6),
        (5, 7),
        (8, 9),
        (10, 10),
    ]
    n = 10
    finder = UnionFindAdvanced(n)
    for v1, v2 in edges:
        finder.union(v1, v2)
    print(finder.rank)
    print(finder.parent)
    print("a and d result: {}".format(finder.find_set(1, 4)))
    print("f anf h result: {}".format(finder.find_set(6, 8)))
