class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        sumVal = 0
        ans = -1

        for num in nums:
            if num < sumVal:
                ans = num + sumVal
            sumVal += num

        return ans