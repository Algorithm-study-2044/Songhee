class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        mod = 10**9 + 7

        idx = dict()
        for i, a in enumerate(arr):
            idx[a] = i

        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                # c = a * b
                c = arr[i]
                a = arr[j]
                b = arr[i] // arr[j]
                if c % a == 0 and b in idx:
                    dp[i] += dp[j] * dp[idx[b]]
                    dp[i] %= mod
        
        return sum(dp) % mod
