class Solution:
    def mySqrt(self, x: int) -> int:
        ans = 0
        while (ans+1)*(ans+1) <= x :
            ans += 1
        return ans