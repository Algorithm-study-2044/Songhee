class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if all(n==0 for n in nums):
            return 0
        nums.sort()
        def subtract(arr):
            arr = [a for a in arr if a != 0]
            arr2 = [a-arr[0] for a in arr if a-arr[0] != 0]
            return arr2
        for i in range(1, len(nums)+1):
            nums = subtract(nums)
            if not nums: return i

        # return len(set(nums)-{0})