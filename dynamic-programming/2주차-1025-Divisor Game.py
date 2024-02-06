class Solution:
    def divisorGame(self, n: int) -> bool:
        dp = [False, False, True, False]
        if n==1 or n==2 or n==3:
            return dp[n]

        for k in range(4, n+1):
            for x in range(1,k):
                if k % x == 0:
                    dp.append(not dp[k-x])
                    break
        print(dp)
        return dp[n]

# ?: return n%2==0 한 줄로 끝나는 코드였음..