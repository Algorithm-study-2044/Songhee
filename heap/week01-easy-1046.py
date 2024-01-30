class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones.sort(reverse=True)
            x, y = stones[0], stones[1]
            if x == y:
                stones = stones[2:]
            else:
                stones = [x-y] + stones[2:]
        if not stones:
            return 0
        else:
            return stones[0]