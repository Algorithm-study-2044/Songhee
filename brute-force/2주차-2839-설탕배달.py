N = int(input())

n5 = N // 5
for x in range(n5, -1, -1):
    res = N - 5*x
    if res%3 == 0:
        y = res // 3
        print(x+y)
        break
    elif x == 0:
        print(-1)