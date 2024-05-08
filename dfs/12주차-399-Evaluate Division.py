class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(set)
        
        # 어떤 수가 다른 수가 되기 위해 나눠야 하는 수를 "간선의 가중치"로 삼는 것
        for (a, b), value in zip(equations, values):
            graph[a].add((b, value))
            graph[b].add((a, 1 / value))
            
        # 만약 query가 ["a", "c"]로 주어진다면 a를 어떤 수로 나눠야 c가 될 수 있는지?
        # 따라서 그래프 상에서 노드 a에서 c까지 가면서 거치는 간선의 가중치를 구하면 됨.
        ans = []
        for a, b in queries:
            ans.append(-1.0)
            if a not in graph:
                continue
            queue = deque()            
            queue.append((a, 1.0))
            visited = set()
            while queue:
                node, val = queue.popleft()
                if node in visited:
                    continue
                if node == b:
                    ans[-1] = val
                    break
                visited.add(node)
                for next_node, next_val in graph[node]:
                    queue.append((next_node, val * next_val))
                
        return ans