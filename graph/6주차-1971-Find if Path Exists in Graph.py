class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        p = [i for i in range(n)]

        def find(x):
            if p[x] == x:
                return x
            return find(p[x])

        def union(x, y):
            px = find(x)
            py = find(y)
            if px != py:
                p[px] = py

        for edge in edges:
            s, d = edge
            union(s, d)

        return find(source) == find(destination)