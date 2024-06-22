class UnionFind:
    def __init__(self, n: int) -> None:
        self.vertex_set = {chr(ord("a") + i): {chr(ord("a") + i)} for i in range(n)}

    def find_set(self, v1: str, v2: str) -> bool:
        return self.vertex_set[v1] == self.vertex_set[v2]

    def union(self, v1: str, v2: str) -> None:
        union_set = self.vertex_set[v1] | self.vertex_set[v2]
        for vertex, component in self.vertex_set.items():
            if v1 in component or v2 in component:
                self.vertex_set[vertex] = union_set
        return


if __name__ == "__main__":
    edges = [
        ("a", "b"),
        ("a", "c"),
        ("b", "c"),
        ("b", "d"),
        ("e", "f"),
        ("e", "g"),
        ("h", "i"),
        ("j", "j"),
    ]
    n = 10
    finder = UnionFind(n)
    for v1, v2 in edges:
        finder.union(v1, v2)
    print(finder.vertex_set)
    print("a and d result: {}".format(finder.find_set("a", "d")))
    print("f anf h result: {}".format(finder.find_set("f", "h")))
