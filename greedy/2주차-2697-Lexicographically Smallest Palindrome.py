class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = list(s)
        n = len(s)-1
        i = 0
        while i < n-i:
            x = s[i]
            y = s[n-i]
            if x < y:
                ans[n-i] = x
            elif x > y:
                ans[i] = y
            i += 1
        return ''.join(ans)