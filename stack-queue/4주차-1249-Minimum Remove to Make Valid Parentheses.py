class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l = 0
        r = 0
        for c in s:
            if c == "(":
                l += 1
            elif c == ")":
                if l > 0:
                    l -= 1
                else:
                    r += 1
        
        return s[::-1].replace("(", "", l)[::-1].replace(")", "", r)