class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        island = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] != '1':
                    continue
                grid[r][c] = '0'
                queue = deque()
                queue.append((r, c))
                while queue:
                    xr, xc = queue.popleft()
                    for (dr, dc) in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                        if 0<=xr+dr<m and 0<=xc+dc<n and grid[xr+dr][xc+dc]=='1':
                            grid[xr+dr][xc+dc] = '0'
                            queue.append((xr+dr, xc+dc))
                island += 1

        return island
        