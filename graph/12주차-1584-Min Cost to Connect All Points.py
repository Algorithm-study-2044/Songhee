class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = defaultdict(list)
        
        for i in range(n):
            x, y = points[i]
            for j in range(i+1, n):
                nx, ny = points[j]
                dist = abs(x-nx) + abs(y-ny)
                
                adj[i].append((dist, j))
                adj[j].append((dist, i))
                
        ans = 0
        visited = set()
        cost_idx = [(0, 0)]
        
        while len(visited) < n:
            cost, idx = heappop(cost_idx)
            if idx in visited:
                continue
                
            visited.add(idx)
            ans += cost
            
            for nei in adj[idx]:
                if nei[1] not in visited:
                    heappush(cost_idx, nei)
                    
        return ans