n = int(input())
blds = list(map(int, input().split()))
cnt = [0 for _ in range(n)]
for i in range(n-1):
    max_slope = -float('inf')
    for j in range(i+1, n):
        slope = (blds[j]-blds[i])/(j-i)
        if slope <= max_slope:
            continue
        max_slope = max(max_slope, slope)
        cnt[i] += 1
        cnt[j] += 1
print(max(cnt))