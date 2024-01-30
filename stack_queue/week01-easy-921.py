from collections import deque
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lp, rp = 0, 0
        for ss in s:
            if ss == '(': 
                rp += 1
            elif ss == ')': 
                if rp: rp -= 1
                else: lp += 1
        return lp+rp