class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        row, col = len(grid),len(grid[0])
        dirs = [(0,0),(-1,0),(0,-1),(1,0),(0,1)]

        island = deque()

        def print_():
            for g in grid:
                print(g)

        def dfs(x,y):
            for dx, dy in dirs:
                if 0<=x+dx<row and 0<=y+dy<col and grid[x+dx][y+dy]==1:
                    grid[x+dx][y+dy]=2
                    island.append([x+dx,y+dy])
                    dfs(x+dx,y+dy)

        #DFS Find the first island and turn all 1 to 2
        def findIsland():
            # 두 개의 섬 중 하나만 바꿔주기.
            for x in range(row):
                for y in range(col):
                    if grid[x][y]:
                        return dfs(x,y)

        # print_()
        findIsland()
        # print_()

        #BFS Expand the island and count step
        step = 0
        while island:
            for _ in range(len(island)):
                x, y = island.popleft()
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<row and 0<=ny<col and grid[nx][ny]!=2:
                        if grid[nx][ny] == 0:
                            grid[nx][ny] = 2
                            island.append([nx,ny])
                        elif grid[nx][ny] == 1:
                            return step
            step+=1

        return step