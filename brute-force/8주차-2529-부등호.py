def check(a, b, op):
  if op == '<':
    if a > b: return False
  if op == '>':
    if a < b: return False
  return True

k = int(input())
ops = input().split()
visited = [0 for i in range(10)]
nums = []

def dfs(num='', cnt=0):
    if cnt == k+1:
        nums.append(num)
        return
    for i in range(10):
        if visited[i]:
            continue
        if cnt == 0 or check(num[cnt-1], str(i), ops[cnt-1]):
            visited[i]=1
            dfs(num+str(i), cnt+1)
            visited[i]=0

dfs()
print(max(nums))
print(min(nums))
