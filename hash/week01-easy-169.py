from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr = Counter(nums)
        for a in arr:
            if arr[a] > len(nums)//2:
                return a
        return -1