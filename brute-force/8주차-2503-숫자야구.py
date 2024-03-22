from itertools import permutations

def match(target, comp):
    s, b = 0, 0
    for i in range(3):
        if target[i] == comp[i]:
            s += 1
        elif target[i] in comp:
            b += 1
    return s, b

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
numbers = list(permutations(["1", "2", "3", "4", "5", "6", "7", "8", "9"], 3))

ans = 0
for num in numbers:
    cnt = 0
    for a in arr:
        s, b = match(num, str(a[0]))
        if (s, b) == (a[1], a[2]):
            cnt += 1
    if cnt == len(arr):
        ans += 1
        
print(ans)