class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False]*len(isConnected)

        def dfs(node):
            for i in range(len(isConnected)):
                if isConnected[node][i]==1 and not visited[i]:
                    visited[i] = True
                    dfs(i)
        res = 0
        for node in range(len(isConnected)):
            if not visited[node]:
                dfs(node)
                res+=1
        return res