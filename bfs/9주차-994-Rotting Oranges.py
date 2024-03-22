class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def isfresh():
            fresh = 0
            for row in grid:
                for col in row:
                    if col == 1:
                        fresh += 1
            if not fresh:
                return False
            return True

        if not isfresh():
            return 0
        
        # 꼭 이렇게 분리할 것이 아니라,
        # while queue:
        #     size = len(queue)
        #     for _ in range(size):
        #         r, c = queue.popleft()
        #         ... 
        # 이런 방식으로 분리해도 된다!
        
        def rotten():
            change_cnt = 0
            queue = deque()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    if grid[r][c]==2:
                        queue.append((r, c))
                        # print(r, c, grid[r][c])
            while queue:
                r, c = queue.popleft()
                for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc]==1:
                        grid[r+dr][c+dc] = 2
                        change_cnt += 1
            return change_cnt

        def show(grid):
            for g in grid:
                print(g)
        
        time = 0
        while isfresh():
            # show(grid)
            time += 1
            change = rotten()
            print()
            if not change and isfresh():
                return -1
        return time
            