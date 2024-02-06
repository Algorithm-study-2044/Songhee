N = int(input())

cnt = 0
for n in range(10000666):
    if '666' in str(n):
        cnt += 1
    if cnt == N:
        print(n)
        break