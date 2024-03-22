row, col, k = list(map(int, input().split()))
graph = [list(input()) for r in range(row)]
answer = 0
def dfs(r, c, cnt=1):
    global answer
    if cnt == k and (r, c) == (0, col-1):
        answer += 1
    for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0<=r+dr<row and 0<=c+dc<col and graph[r+dr][c+dc]=='.':
            graph[r+dr][c+dc] = 'T'
            dfs(r+dr, c+dc, cnt+1)
            graph[r+dr][c+dc] = '.'
graph[row-1][0] = 'T'
dfs(row-1, 0)
print(answer)