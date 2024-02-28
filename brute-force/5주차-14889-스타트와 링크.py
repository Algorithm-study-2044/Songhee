# 다시 풀기 (dfs, combination 방식)

def dfs(depth, idx):
    global min_diff
    if depth == n//2:
        a, b = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    a += graph[i][j]
                elif not visited[i] and not visited[j]:
                    b += graph[i][j]
        min_diff = min(min_diff, abs(a-b))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]

min_diff = int(1e9)

dfs(0, 0)

print(min_diff)