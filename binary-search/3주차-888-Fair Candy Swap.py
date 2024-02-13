class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        fair = (sum(aliceSizes) + sum(bobSizes))//2
        bob = set(bobSizes)
        for alice in aliceSizes:
            res = fair-sum(aliceSizes)+alice
            if res in bob:
                return [alice, res]