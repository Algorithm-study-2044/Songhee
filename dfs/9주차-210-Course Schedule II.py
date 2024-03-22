class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 위상정렬 문제
        edges = [0 for _ in range(numCourses)] # ingoing edge count
        graph = [[] for _ in range(numCourses)] # outgoing edges
        for prereq in prerequisites:
            t = prereq[0]
            f = prereq[1]
            edges[t] += 1
            graph[f].append(t)

        queue = deque() # enqueue nodes if ingoing edge count == 0
        for i in range(len(edges)):
            if not edges[i]:
                queue.append(i)

        ans = []
        while queue:
            x = queue.popleft()
            ans.append(x)
            adj = graph[x]
            for a in adj:
                edges[a] -= 1
                if not edges[a]:
                    queue.append(a)
                    
        # 33 / 45 testcases passed, impossible case 처리
        if len(ans) != numCourses:
            return []
        return ans