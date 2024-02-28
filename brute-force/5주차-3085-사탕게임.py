# check board code...
def check(data):
    n = len(data)
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if data[i][j] == data[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if data[j][i] == data[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
    return max_cnt


n = int(input())
g = [list(input()) for _ in range(n)]

ans = 0
for r in range(n):
    for c in range(n):
        if r < n-1:
            g[r][c], g[r+1][c] = g[r+1][c], g[r][c]
            ans = max(ans, check(g))
            g[r][c], g[r+1][c] = g[r+1][c], g[r][c]
        if c < n-1:
            g[r][c], g[r][c+1] = g[r][c+1], g[r][c]
            ans = max(ans, check(g))
            g[r][c], g[r][c+1] = g[r][c+1], g[r][c]

print(ans)