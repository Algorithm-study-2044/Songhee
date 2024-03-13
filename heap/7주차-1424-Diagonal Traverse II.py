class Solution:
    # heap: 속도 느림
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        arr = []
        for r in range(len(nums)):
            for c in range(len(nums[r])):
                arr.append((r+c, c, r, nums[r][c]))
        heapq.heapify(arr)
        ans = []
        while arr:
            a = heapq.heappop(arr)[3]
            print(a)
            ans.append(a)
        return ans

    # bfs: 굳이 heap을 써서 풀 이유가 없는듯함
    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0,0)])
        ans = []

        while queue: 
            r, c = queue.popleft()
            ans.append(nums[r][c])

            if c == 0 and r + 1 < len(nums): 
                queue.append((r+1, c))
            if c + 1 < len(nums[r]): 
                queue.append((r, c+1))
        return ans