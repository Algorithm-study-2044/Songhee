class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = ceil(sum(piles)/h)
        right = ceil(sum(piles)/(h-len(piles)+1))

        while left < right:
            mid = (left + right) // 2
            time = 0
            for pile in piles:
                time += ceil(pile/mid)
            if time > h:
                left = mid + 1
            else:
                right = mid

        return left