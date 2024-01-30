class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = sorted(nums, reverse=True)[:2]
        return (arr[0]-1)*(arr[1]-1)