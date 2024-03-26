class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # 위상정렬 문제
        ingoing = [0 for _ in range(numCourses)]
        outgoing = [[] for _ in range(numCourses)]
        for prereq in prerequisites:
            f = prereq[0]
            t = prereq[1]
            ingoing[t] += 1
            outgoing[f].append(t)

        queue = deque()
        for i, x in enumerate(ingoing):
            if x == 0:
                queue.append(i)
        order = []
        while queue:
            x = queue.popleft()
            order.append(x)
            for y in outgoing[x]:
                ingoing[y] -= 1
                if ingoing[y] == 0:
                    queue.append(y)

        return len(order) == numCourses
        
        