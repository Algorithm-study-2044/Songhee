class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        subs = ''
        i = 0
        l = 0
        r = 0
        while i < len(s):
            if s[i] == 'L':
                l += 1
            else:
                r += 1
            subs += s[i]
            if l == r:
                ans += 1
                l = 0
                r = 0
            i += 1
        return ans