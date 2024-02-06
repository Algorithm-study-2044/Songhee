class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [c for c in cost]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[len(cost)-1], dp[len(cost)-2])