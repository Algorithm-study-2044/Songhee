class Solution:
    def minOperations(self, n: int) -> int:
        # 54 = 32 + 16 + 4 + 2 = 110110
        # 71 = 64 + 4 + 2 + 1 = 1000111

        ans = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif n & 2:
                n += 1
                ans += 1
            else:
                n -= 1
                ans += 1

        return ans