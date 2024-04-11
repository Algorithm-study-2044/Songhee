n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for __ in range(n)]

def is_valid(r, c):
    for dr, dc in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
        if 0<=r+dr<n and 0<=c+dc<n and not visited[r+dr][c+dc]:
            continue
        else:
            return False
    return True

def get_cost_of(r, c):
    cost = 0
    for dr, dc in [(0, 0), (0, 1), (1, 0), (0, -1), (-1, 0)]:
        cost += g[r+dr][c+dc]
    return cost

def dfs(x, cnt, cost_sum):
    global min_cost
    if cnt == 3:
        min_cost = min(min_cost, cost_sum)
        return
    for i in range(x, n-1):
        for j in range(1, n-1):
            if is_valid(i, j):
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
                    visited[i + dx][j + dy] = False
                dfs(i, cnt+1, cost_sum + get_cost_of(i, j))
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0):
                    visited[i + dx][j + dy] = True

min_cost = float('inf')
dfs(1, 0, 0)
print(min_cost)