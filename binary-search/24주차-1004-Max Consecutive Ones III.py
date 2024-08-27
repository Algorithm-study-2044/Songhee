class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        s = 0
        e = 0
        z = 0
        while e < len(nums):
            if nums[e] == 0:
                z += 1
            e += 1
            if z > k:
                if nums[s] == 0:
                    z -= 1
                s += 1
        return e - s