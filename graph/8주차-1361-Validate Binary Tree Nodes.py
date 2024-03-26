class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        # 무향 그래프 cycle 찾기: union-find
        # 유향 그래프 cycle 찾기: dfs

        graph = [[] for _ in range(n)]
        root = set([i for i in range(n)])
        try:
            for x in range(n):
                l = leftChild[x]
                r = rightChild[x]
                if l != -1:
                    graph[x].append(l)
                    root.remove(l)
                if r != -1:
                    graph[x].append(r)
                    root.remove(r)
        except:
            return False
        
        if len(root) != 1:
            return False
        
        def dfs(x):
            nonlocal cnt
            nonlocal n
            if cnt > n:
                return
            for y in graph[x]:
                cnt += 1
                dfs(y)

        # 30/51 time limit exceeded -> find root!
        # for i in range(n):
        #     cnt = 1
        #     dfs(i)
        #     if cnt == n:
        #         return True

        cnt = 1
        dfs(root.pop())

        return cnt == n