n = int(input())

# 와.. 이렇게 노가다라고?
for num in range(1, n+1):
    arr = list(map(int, str(num)))
    tmp = sum(arr) + num
    if tmp == n:
        print(num)
        break
    if num == n:
        print(0) 