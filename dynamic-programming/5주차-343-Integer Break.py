# 풀이 참고, 2개의 곱셈으로 나눠 단순화 해서 품

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        for i in range(1, n+1):
            if i==1:
                dp[i]=1
                continue
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], j*dp[i-j], j*(i-j))
        return dp[n]