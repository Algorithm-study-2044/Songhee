class Solution:
    def numSquares1(self, n: int) -> int:
        # dp 문제인 것 같은데..
        dp = [0 for _ in range(14)]
        dp[0] = 0
        dp[1] = 1 # 1
        dp[2] = 2 # 1+1
        dp[3] = 3 # 1+1+1
        dp[4] = 1 # 4
        dp[5] = 2 # 4+1
        dp[6] = 3 # 4+1+1
        dp[7] = 4 # 4+1+1+1
        dp[8] = 2 # 4+4
        dp[9] = 1 # 9
        dp[10] = 2 # 9+1
        dp[11] = 3 # 9+1+1
        dp[12] = 3 # 9+1+1+1 or 4+4+4
        dp[13] = 2 # 9+4
        
        if n < 14:
            return dp[n]

        def find(n, x):
            min_dp = n
            for xx in range(1, x+1):
                if n < xx*xx:
                    break
                min_dp = min(min_dp, dp[n-xx*xx])
            return min_dp
        
        x = 3
        for i in range(14, n+1):
            if i == (x+1)*(x+1):
                dp.append(1)
                x += 1
            else:
                dp.append(1+find(i, x))
        return dp[n]

    # solution 참고: 깔끔하게 풀었음
    def numSquares(self, n: int) -> int:
        counts = [c for c in range(n + 1)]
        for num in range(1, n + 1):
            k = int(num**0.5)
            min_count = min(counts[num - i**2] for i in range(1, k + 1))
            counts[num] = min_count + 1
        return counts[n]