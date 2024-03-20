class Node:
    def __init__(self):
        self.connected = []
        self.inbound = 0

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [Node() for _ in range(numCourses)]
        left = numCourses
        for i in prerequisites:
            graph[i[1]].connected.append(i[0])
            graph[i[0]].inbound += 1

        q = deque()

        for node in graph:
            if node.inbound == 0: q.append(node)

        while len(q) != 0:
            node: Node = q.popleft()
            left -= 1
            for c in node.connected:
                graph[c].inbound -= 1
                if graph[c].inbound == 0:
                    q.append(graph[c])

        if left == 0: return True
        else: return False