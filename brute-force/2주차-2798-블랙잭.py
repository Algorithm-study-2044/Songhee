n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))

ans = arr[0] + arr[1] + arr[2]
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            tmp = arr[i] + arr[j] + arr[k]
            if abs(tmp-m) < abs(ans-m) and tmp <= m:
                ans = tmp

print(ans)