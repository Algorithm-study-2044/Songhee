ROB = 0
NOT_ROB = 1

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [[0, 0] for _ in range(nums)]
        dp[0][ROB] = nums[0]
        for i in range(1, len(nums)):
            dp[i][ROB] = dp[i-1][NOT_ROB] + nums[i]
            dp[i][NOT_ROB] = max(dp[i-1][ROB], dp[i-1][NOT_ROB])

        return max(dp[len(nums)-1])